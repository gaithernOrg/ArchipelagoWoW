import logging
from typing import List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import WOWItem, WOWItemData, event_item_table, get_items_by_category, item_table, item_name_groups
from .Locations import WOWLocation, location_table, get_locations_by_category, location_name_groups
from .Options import WOWOptions, WOW_option_groups
from .Regions import create_regions
from .Rules import set_rules
from .Presets import WOW_option_presets
from worlds.LauncherComponents import Component, components, Type, launch_subprocess


def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="WOW Client")


components.append(Component("WOW Client", "WOWClient", func=launch_client, component_type=Type.CLIENT))


class WOWWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the World of Warcraft Randomizer software on your computer."
            "This guide covers single-player, multiworld, and related software.",
            "English",
            "WOW_en.md",
            "WOW/en",
            ["Gicu"]
    )]
    option_groups = WOW_option_groups
    options_presets = WOW_option_presets


class WOWWorld(World):
    """
    World of Warcraft (WoW) is a 2004 massively multiplayer 
    online role-playing (MMORPG) video game produced by Blizzard Entertainment.
    """
    game = "World of Warcraft"
    options_dataclass = WOWOptions
    options: WOWOptions
    topology_present = True
    web = WOWWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    fillers = {}
    fillers.update(get_items_by_category("Filler"))

    def create_items(self):
        self.place_predetermined_items()
        item_pool = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        
        precollected_items = ["Northshire Valley"]
        for precollected_item in precollected_items:
            self.multiworld.push_precollected(self.create_item(precollected_item))
        
        non_filler_item_categories = ["SubZone", "Equipment", "Macguffin"]
        for name, data in item_table.items():
            quantity = data.max_quantity
            if data.category not in non_filler_item_categories:
                continue
            if name in precollected_items:
                continue
            if name == "Honor":
                item_pool += [self.create_item(name) for _ in range(0, self.options.honor_in_pool)]
            else:
                item_pool += [self.create_item(name) for _ in range(0, quantity)]
        
        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))
        
        self.multiworld.itempool += item_pool

    def place_predetermined_items(self) -> None:
        self.get_location("Become a Champion of Azeroth").place_locked_item(self.create_event("Victory"))

    def get_filler_item_name(self) -> str:
        weights = [data.weight for data in self.fillers.values()]
        return self.random.choices([filler for filler in self.fillers.keys()], weights)[0]
    
    def fill_slot_data(self) -> dict:
        slot_data = {"honor_to_win": int(self.options.honor_to_win)}
        return slot_data

    def create_item(self, name: str) -> WOWItem:
        data = item_table[name]
        return WOWItem(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> WOWItem:
        data = event_item_table[name]
        return WOWItem(name, data.classification, data.code, self.player)

    def set_rules(self):
        set_rules(self)

    def create_regions(self):
        create_regions(self.multiworld, self.player, self.options)
