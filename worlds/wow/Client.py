from __future__ import annotations
import os
import json
import sys
import asyncio
import shutil
import logging
import re
import time
from tkinter import filedialog
from calendar import timegm

import ModuleUpdate
ModuleUpdate.update()

import Utils
item_num = 1

logger = logging.getLogger("Client")

if __name__ == "__main__":
    Utils.init_logging("WOWClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop


def check_stdin() -> None:
    if Utils.is_windows and sys.stdin:
        print("WARNING: Console input is not routed reliably on Windows, use the GUI instead.")

class WOWClientCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)
    
    

class WOWContext(CommonContext):
    command_processor: int = WOWClientCommandProcessor
    game = "World of Warcraft"
    items_handling = 0b111  # full remote
    subzones = []
    equipment = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    honor = 0
    required_honor = 999
    last_sent_lua_txt = ""
    last_sent_locations = []
    communication_file_last_updated = None
    saved_variables_location = str(filedialog.askopenfilename(title = "Select your wow_ap.lua saved variable file"))
    player_object_location = str(filedialog.askopenfilename(title = "Select your player_object.lua file in the mod folder"))

    def __init__(self, server_address, password):
        super(WOWContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        self.hinted_synth_location_ids = False
        self.slot_data = {}

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(WOWContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(WOWContext, self).connection_closed()
        global item_num
        item_num = 1

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(WOWContext, self).shutdown()
        global item_num
        item_num = 1

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:
            # Handle Slot Data
            self.slot_data = args['slot_data']

        if cmd in {"ReceivedItems"}:
            start_index = args["index"]
            if start_index != len(self.items_received):
                for item in args['items']:
                    item_id = NetworkItem(*item).item
                    if item_id >= 221522_1000000 and item_id < 221522_2000000: # SubZone
                        self.subzones.append(item_id % 221522_1000000)
                    elif item_id > 221522_2000000 and item_id < 221522_3000000: # Equipment
                        equipment_index = (item_id % 221522_2000000) - 1
                        self.equipment[equipment_index] = self.equipment[equipment_index] + 1
            lua_txt = self.create_player_object_lua_string()
            if lua_txt != self.last_sent_lua_txt:
                self.overwrite_data_file(lua_txt)
                self.last_sent_lua_txt = lua_txt

        if cmd in {"RoomUpdate"}:
            if "checked_locations" in args:
                for ss in self.checked_locations:
                    pass

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class WOWManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago WOW Client"

        self.ui = WOWManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def create_player_object_lua_string(self):
        lua_txt = """_G["ap_player"] = {}
_G["ap_player"]["Highest Quality"] = {"""
        for equipment_rarity_unlocked in self.equipment:
            lua_txt = lua_txt + str(equipment_rarity_unlocked) + ","
        lua_txt = lua_txt[:-1] + """}
_G["ap_player"]["Available SubZones"] = {"""
        for subzone in self.subzones:
            lua_txt = lua_txt + str(subzone) + ","
        lua_txt = lua_txt[:-1] + """}"""
        return lua_txt
    
    def overwrite_data_file(self, text):
        f = open(self.player_object_location, "w")
        f.write(text)
        f.close()


async def game_watcher(ctx: WOWContext):
    from .Locations import lookup_id_to_name
    while not ctx.exit_event.is_set():
        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        victory = False
        should_read = False
        file_last_modified_date = time.localtime((os.stat(ctx.saved_variables_location).st_mtime))
        if ctx.communication_file_last_updated is None:
            should_read = True
        elif ctx.communication_file_last_updated != file_last_modified_date:
            should_read = True
        if should_read:
            f = open(ctx.saved_variables_location, "r")
            file_contents = f.read().splitlines()
            f.close()
            for line in file_contents:
                if len(line) > 0:
                    if line[0].isdigit():
                        sending.append(int(line[:-1]) + 221523_0000000)
                    elif line.startswith("Honor"):
                        if "honor_to_win" in ctx.slot_data.keys():
                            if int(line.replace("Honor = ", "")) >= ctx.slot_data["honor_to_win"]:
                                victory = True
            ctx.communication_file_last_updated = file_last_modified_date
        if sending != ctx.last_sent_locations or len(sending) == 0:
            ctx.locations_checked = sending
            message = [{"cmd": 'LocationChecks', "locations": sending}]
            await ctx.send_msgs(message)
            if not ctx.finished_game and victory:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                ctx.finished_game = True
            ctx.last_sent_locations = sending.copy()
        await asyncio.sleep(1)


def launch():
    async def main(args):
        ctx = WOWContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="WOWProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="WOW Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
