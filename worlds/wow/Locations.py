from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class WOWLocation(Location):
    game: str = "World of Warcraft"


class WOWLocationData(NamedTuple):
    category: str
    code: int


def get_locations_by_category(category: str) -> Dict[str, WOWLocationData]:
    location_dict: Dict[str, WOWLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, WOWLocationData] = {
    "Elwynn Forest - Beating them Back!":      WOWLocationData("Elwynn Forest",  221523_0028757),
    "Elwynn Forest - Lions for Lambs":         WOWLocationData("Elwynn Forest",  221523_0028759),
    "Elwynn Forest - Join the Battle!":        WOWLocationData("Elwynn Forest",  221523_0028780),
    "Elwynn Forest - They Sent Assassins":     WOWLocationData("Elwynn Forest",  221523_0028791),
    "Elwynn Forest - The Rear is Clear":       WOWLocationData("Elwynn Forest",  221523_0028817),
    "Elwynn Forest - Blackrock Invasion":      WOWLocationData("Elwynn Forest",  221523_0026389),
    "Elwynn Forest - Extinguishing Hope":      WOWLocationData("Elwynn Forest",  221523_0026391),
    "Elwynn Forest - Ending the Invasion!":    WOWLocationData("Elwynn Forest",  221523_0026390),
    "Elwynn Forest - Report to Goldshire":     WOWLocationData("Elwynn Forest",  221523_0000051),
    "Elwynn Forest - Fear No Evil":            WOWLocationData("Elwynn Forest",  221523_0028806),
    "Elwynn Forest - Rest and Relaxation":     WOWLocationData("Elwynn Forest",  221523_0037112),
    "Elwynn Forest - Gold Dust Exchange":      WOWLocationData("Elwynn Forest",  221523_0000047),
    "Elwynn Forest - Kobold Candles":          WOWLocationData("Elwynn Forest",  221523_0000060),
    "Elwynn Forest - The Fargodeep Mine":      WOWLocationData("Elwynn Forest",  221523_0000062),
    "Elwynn Forest - The Jasperlode Mine":     WOWLocationData("Elwynn Forest",  221523_0000076),
    "Elwynn Forest - A Visit With Maybell":    WOWLocationData("Elwynn Forest",  221523_0026150),
    "Elwynn Forest - Young Lovers":            WOWLocationData("Elwynn Forest",  221523_0000106),
    "Elwynn Forest - Speak with Gramma":       WOWLocationData("Elwynn Forest",  221523_0000111),
    "Elwynn Forest - Note to William":         WOWLocationData("Elwynn Forest",  221523_0000107),
    "Elwynn Forest - Collecting Kelp":         WOWLocationData("Elwynn Forest",  221523_0000112),
    "Elwynn Forest - The Escape":              WOWLocationData("Elwynn Forest",  221523_0000114),
    "Elwynn Forest - Princess Must Die!":      WOWLocationData("Elwynn Forest",  221523_0000088),
    "Elwynn Forest - Lost Necklace":           WOWLocationData("Elwynn Forest",  221523_0000085),
    "Elwynn Forest - Pie for Billy":           WOWLocationData("Elwynn Forest",  221523_0000086),
    "Elwynn Forest - Back to Billy":           WOWLocationData("Elwynn Forest",  221523_0000084),
    "Elwynn Forest - Goldtooth":               WOWLocationData("Elwynn Forest",  221523_0000087),
    "Elwynn Forest - A Fishy Peril":           WOWLocationData("Elwynn Forest",  221523_0000040),
    "Elwynn Forest - Further Concerns":        WOWLocationData("Elwynn Forest",  221523_0000035),
    "Elwynn Forest - Find the Lost Guards":    WOWLocationData("Elwynn Forest",  221523_0000037),
    "Elwynn Forest - Discover Rolf's Fate":    WOWLocationData("Elwynn Forest",  221523_0000045),
    "Elwynn Forest - Report to Thomas":        WOWLocationData("Elwynn Forest",  221523_0000071),
    "Elwynn Forest - Cloth and Leather Armor": WOWLocationData("Elwynn Forest",  221523_0000059),
    "Elwynn Forest - Bounty on Murlocs":       WOWLocationData("Elwynn Forest",  221523_0000046),
    "Elwynn Forest - WANTED: James Clark":     WOWLocationData("Elwynn Forest",  221523_0026152),
    "Elwynn Forest - Protect the Frontier":    WOWLocationData("Elwynn Forest",  221523_0000052),
    "Elwynn Forest - Fine Linen Goods":        WOWLocationData("Elwynn Forest",  221523_0000083),
    "Elwynn Forest - A Bundle of Trouble":     WOWLocationData("Elwynn Forest",  221523_0005545),
    "Elwynn Forest - The Collector":           WOWLocationData("Elwynn Forest",  221523_0000123),
    "Elwynn Forest - Manhunt":                 WOWLocationData("Elwynn Forest",  221523_0000147),
    "Elwynn Forest - Riverpaw Gnoll Bounty":   WOWLocationData("Elwynn Forest",  221523_0000011),
    "Elwynn Forest - WANTED: \"Hogger\"":      WOWLocationData("Elwynn Forest",  221523_0000176),
}

event_location_table: Dict[str, WOWLocationData] = {}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}


#Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set()
    location_name_groups[category].add(location)
