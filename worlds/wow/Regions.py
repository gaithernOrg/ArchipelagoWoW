from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import WOWLocation, location_table


class WOWRegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int, options):
    regions: Dict[str, WOWRegionData] = {
        "Menu":                  WOWRegionData([], ["Northshire Valley", "Other"]),
        "Northshire Valley":     WOWRegionData([], ["Elwynn Forest"]),
        "Elwynn Forest":         WOWRegionData([], ["Goldshire", "Dwarven District", "Old Town", "The Maclure Vineyards", "The Stonefield Farm", "Westbrook Garrison", "Stone Cairn Lake", "Forest's Edge", "Eastvale Logging Camp"]),
        "Goldshire":             WOWRegionData([], ["Lion's Pride Inn"]),
        "Lion's Pride Inn":      WOWRegionData([], []),
        "Dwarven District":      WOWRegionData([], []),
        "Old Town":              WOWRegionData([], []),
        "The Maclure Vineyards": WOWRegionData([], []),
        "The Stonefield Farm":   WOWRegionData([], []),
        "Westbrook Garrison":    WOWRegionData([], []),
        "Stone Cairn Lake":      WOWRegionData([], []),
        "Forest's Edge":         WOWRegionData([], []),
        "Eastvale Logging Camp": WOWRegionData([], []),
        "Other":                 WOWRegionData([], []),
    }

    # Set up locations
    regions["Northshire Valley"].locations.append("Northshire Valley - Beating Them Back!")
    regions["Northshire Valley"].locations.append("Northshire Valley - Blackrock Invasion")
    regions["Northshire Valley"].locations.append("Northshire Valley - Ending the Invasion")
    regions["Northshire Valley"].locations.append("Northshire Valley - Extinguishing Hope")
    regions["Northshire Valley"].locations.append("Northshire Valley - Fear No Evil")
    regions["Northshire Valley"].locations.append("Northshire Valley - Join the Battle!")
    regions["Northshire Valley"].locations.append("Northshire Valley - Lions for Lambs")
    regions["Northshire Valley"].locations.append("Northshire Valley - Report to Goldshire")
    regions["Northshire Valley"].locations.append("Northshire Valley - The Rear is Clear")
    regions["Northshire Valley"].locations.append("Northshire Valley - They Sent Assassins")
    regions["Eastvale Logging Camp"].locations.append("Eastvale Logging Camp - A Bundle of Trouble")
    regions["Eastvale Logging Camp"].locations.append("Eastvale Logging Camp - Fine Linen Goods")
    regions["Eastvale Logging Camp"].locations.append("Eastvale Logging Camp - Manhunt")
    regions["Eastvale Logging Camp"].locations.append("Eastvale Logging Camp - The Collector")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Bounty on Murlocs")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Cloth and Leather Armor")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Find the Lost Guards")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Protect the Frontier")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Report to Thomas")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - Rest and Relaxation")
    regions["Elwynn Forest"].locations.append("Elwynn Forest - WANTED: James Clark")
    regions["Forest's Edge"].locations.append("Forest's Edge - Furlbrow's Deed")
    regions["Forest's Edge"].locations.append("Forest's Edge - WANTED: \"Hogger\"")
    regions["Goldshire"].locations.append("Goldshire - A Fishy Peril")
    regions["Goldshire"].locations.append("Goldshire - A Swift Message")
    regions["Goldshire"].locations.append("Goldshire - Continue to Stormwind")
    regions["Goldshire"].locations.append("Goldshire - Further Concerns")
    regions["Goldshire"].locations.append("Goldshire - Gold Dust Exchange")
    regions["Goldshire"].locations.append("Goldshire - Kobold Candles")
    regions["Goldshire"].locations.append("Goldshire - The Fargodeep Mine")
    regions["Goldshire"].locations.append("Goldshire - The Jasperlode Mine")
    regions["Lion's Pride Inn"].locations.append("Lion's Pride Inn - Collecting Kelp")
    regions["Lion's Pride Inn"].locations.append("Lion's Pride Inn - The Escape")
    regions["Stone Cairn Lake"].locations.append("Stone Cairn Lake - Discover Rolf's Fate")
    regions["The Maclure Vineyards"].locations.append("The Maclure Vineyards - Goldtooth")
    regions["The Maclure Vineyards"].locations.append("The Maclure Vineyards - Pie for Billy")
    regions["The Maclure Vineyards"].locations.append("The Maclure Vineyards - Young Lovers")
    regions["The Stonefield Farm"].locations.append("The Stonefield Farm - Back to Billy")
    regions["The Stonefield Farm"].locations.append("The Stonefield Farm - Lost Necklace")
    regions["The Stonefield Farm"].locations.append("The Stonefield Farm - Note to William")
    regions["The Stonefield Farm"].locations.append("The Stonefield Farm - Speak with Gramma")
    regions["Westbrook Garrison"].locations.append("Westbrook Garrison - Riverpaw Gnoll Bounty")
    
    regions["Other"].locations.append("Become a Champion of Azeroth")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    multiworld.get_entrance("Northshire Valley", player).connect(multiworld.get_region("Northshire Valley", player))
    multiworld.get_entrance("Eastvale Logging Camp", player).connect(multiworld.get_region("Eastvale Logging Camp", player))
    multiworld.get_entrance("Elwynn Forest", player).connect(multiworld.get_region("Elwynn Forest", player))
    multiworld.get_entrance("Forest's Edge", player).connect(multiworld.get_region("Forest's Edge", player))
    multiworld.get_entrance("Goldshire", player).connect(multiworld.get_region("Goldshire", player))
    multiworld.get_entrance("Lion's Pride Inn", player).connect(multiworld.get_region("Lion's Pride Inn", player))
    multiworld.get_entrance("Dwarven District", player).connect(multiworld.get_region("Dwarven District", player))
    multiworld.get_entrance("Old Town", player).connect(multiworld.get_region("Old Town", player))
    multiworld.get_entrance("Stone Cairn Lake", player).connect(multiworld.get_region("Stone Cairn Lake", player))
    multiworld.get_entrance("The Maclure Vineyards", player).connect(multiworld.get_region("The Maclure Vineyards", player))
    multiworld.get_entrance("The Stonefield Farm", player).connect(multiworld.get_region("The Stonefield Farm", player))
    multiworld.get_entrance("Westbrook Garrison", player).connect(multiworld.get_region("Westbrook Garrison", player))
    multiworld.get_entrance("Other", player).connect(multiworld.get_region("Other", player))

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
