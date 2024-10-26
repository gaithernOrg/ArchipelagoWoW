from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import WOWLocation, location_table


class WOWRegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int, options):
    regions: Dict[str, WOWRegionData] = {
        "Menu":          WOWRegionData([], ["Elwynn Forest"]),
        "Elwynn Forest": WOWRegionData([], [])
    }

    # Set up locations
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Beating them Back!")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Lions for Lambs")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Join the Battle!")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - They Sent Assassins")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - The Rear is Clear")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Blackrock Invasion")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Extinguishing Hope")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Ending the Invasion!")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Report to Goldshire")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Fear No Evil")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Rest and Relaxation")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Gold Dust Exchange")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Kobold Candles")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - The Fargodeep Mine")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - The Jasperlode Mine")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - A Visit With Maybell")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Young Lovers")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Speak with Gramma")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Note to William")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Collecting Kelp")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - The Escape")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Princess Must Die!")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Lost Necklace")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Pie for Billy")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Back to Billy")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Goldtooth")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - A Fishy Peril")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Further Concerns")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Find the Lost Guards")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Discover Rolf's Fate")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Report to Thomas")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Cloth and Leather Armor")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Bounty on Murlocs")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - WANTED: James Clark")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Protect the Frontier")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Fine Linen Goods")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - A Bundle of Trouble")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - The Collector")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Manhunt")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Riverpaw Gnoll Bounty")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - WANTED: \"Hogger\"")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    multiworld.get_entrance("Elwynn Forest", player).connect(multiworld.get_region("Elwynn Forest", player))

def create_region(multiworld: MultiWorld, player: int, name: str, data: WOWRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = WOWLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    if data.region_exits:
        for exit in data.region_exits:
            entrance = Entrance(player, exit, region)
            region.exits.append(entrance)

    return region
