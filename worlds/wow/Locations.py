from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class WOWLocation(Location):
    game: str = "World of Warcraft"


class WOWLocationData(NamedTuple):
    category: str
    quest_turn_in_category: str
    code: int


def get_locations_by_category(category: str) -> Dict[str, WOWLocationData]:
    location_dict: Dict[str, WOWLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict


location_table: Dict[str, WOWLocationData] = {
    # Northshire
    "Northshire Valley - Beating Them Back!":                      WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028766),
    "Northshire Valley - Blackrock Invasion":                      WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0026389),
    "Northshire Valley - Ending the Invasion":                     WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0026390),
    "Northshire Valley - Extinguishing Hope":                      WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0026391),
    "Northshire Valley - Fear No Evil":                            WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028813),
    "Northshire Valley - Join the Battle!":                        WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028789),
    "Northshire Valley - Lions for Lambs":                         WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028774),
    "Northshire Valley - Report to Goldshire":                     WOWLocationData("Northshire Valley",     "Goldshire",              221523_0000054),
    "Northshire Valley - The Rear is Clear":                       WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028823),
    "Northshire Valley - They Sent Assassins":                     WOWLocationData("Northshire Valley",     "Northshire Valley",      221523_0028797),
    
    # Elwynn Forest
    "Eastvale Logging Camp - A Bundle of Trouble":                 WOWLocationData("Eastvale Logging Camp", "Eastvale Logging Camp",  221523_0005545),
    "Goldshire - A Fishy Peril":                                   WOWLocationData("Goldshire",             "Goldshire",              221523_0000040),
    "Goldshire - A Swift Message":                                 WOWLocationData("Goldshire",             "Goldshire",              221523_0026393),
    "The Stonefield Farm - Back to Billy":                         WOWLocationData("The Stonefield Farm",   "The Maclure Vineyards",  221523_0000084),
    "Elwynn Forest - Bounty on Murlocs":                           WOWLocationData("Elwynn Forest",         "Elwynn Forest",          221523_0000046),
    "Elwynn Forest - Cloth and Leather Armor":                     WOWLocationData("Elwynn Forest",         "Eastvale Logging Camp",  221523_0000059),
    "Lion's Pride Inn - Collecting Kelp":                          WOWLocationData("Lion's Pride Inn",      "Lion's Pride Inn",       221523_0000112),
    "Goldshire - Continue to Stormwind":                           WOWLocationData("Goldshire",             "Old Town",               221523_0026394),
    "Stone Cairn Lake - Discover Rolf's Fate":                     WOWLocationData("Stone Cairn Lake",      "Stone Cairn Lake",       221523_0000045),
  # "Goldshire - Elmore's Task":                                   WOWLocationData("Goldshire",             "Dwarven District",       221523_0001097), Breadcrumb Quest
    "Elwynn Forest - Find the Lost Guards":                        WOWLocationData("Elwynn Forest",         "Stone Cairn Lake",       221523_0000037),
    "Eastvale Logging Camp - Fine Linen Goods":                    WOWLocationData("Eastvale Logging Camp", "Eastvale Logging Camp",  221523_0000083),
    "Forest's Edge - Furlbrow's Deed":                             WOWLocationData("Forest's Edge",         "The Jansen Stead",       221523_0000184),
    "Goldshire - Further Concerns":                                WOWLocationData("Goldshire",             "Elwynn Forest",          221523_0000035),
    "Goldshire - Gold Dust Exchange":                              WOWLocationData("Goldshire",             "Goldshire",              221523_0000047),
    "The Maclure Vineyards - Goldtooth":                           WOWLocationData("The Maclure Vineyards", "The Stonefield Farm",    221523_0000087),
  # "Goldshire - Hero's Call: Westfall!":                          WOWLocationData("Goldshire",              "The Jansen Stead",      221523_0026378), Breadcrumb Quest
    "Goldshire - Kobold Candles":                                  WOWLocationData("Goldshire",              "Goldshire",             221523_0000060),
    "The Stonefield Farm - Lost Necklace":                         WOWLocationData("The Stonefield Farm",    "The Maclure Vineyards", 221523_0000085),
    "Eastvale Logging Camp - Manhunt":                             WOWLocationData("Eastvale Logging Camp",  "Eastvale Logging Camp", 221523_0000147),
    "The Stonefield Farm - Note to William":                       WOWLocationData("The Stonefield Farm",    "Lion's Pride Inn",      221523_0000107),
    "The Maclure Vineyards - Pie for Billy":                       WOWLocationData("The Maclure Vineyards",  "The Stonefield Farm",   221523_0000086),
    "Elwynn Forest - Protect the Frontier":                        WOWLocationData("Elwynn Forest",          "Elwynn Forest",         221523_0000052),
    "Elwynn Forest - Report to Thomas":                            WOWLocationData("Stone Cairn Lake",       "Elwynn Forest",         221523_0000071),
    "Elwynn Forest - Rest and Relaxation":                         WOWLocationData("Elwynn Forest",          "Lion's Pride Inn",      221523_0037112),
    "Westbrook Garrison - Riverpaw Gnoll Bounty":                  WOWLocationData("Westbrook Garrison",     "Westbrook Garrison",    221523_0000011),
    "The Stonefield Farm - Speak with Gramma":                     WOWLocationData("The Stonefield Farm",    "The Stonefield Farm",   221523_0000111),
    "Eastvale Logging Camp - The Collector":                       WOWLocationData("Eastvale Logging Camp",  "Eastvale Logging Camp", 221523_0000123),
    "Lion's Pride Inn - The Escape":                               WOWLocationData("Lion's Pride Inn",       "The Maclure Vineyards", 221523_0000114),
    "Goldshire - The Fargodeep Mine":                              WOWLocationData("Goldshire",              "Goldshire",             221523_0000062),
    "Goldshire - The Jasperlode Mine":                             WOWLocationData("Goldshire",              "Goldshire",             221523_0000076),
    "Forest's Edge - WANTED: \"Hogger\"":                          WOWLocationData("Forest's Edge",          "Goldshire",             221523_0000176),
    "Elwynn Forest - WANTED: James Clark":                         WOWLocationData("Elwynn Forest",          "Eastvale Logging Camp", 221523_0026152),
   #"Goldshire - Westbrook Garrison Needs Your Help!":             WOWLocationData("Goldshire",              "Westbrook Garrison",    221523_0000239), Breadcrumb Quest
    "The Maclure Vineyards - Young Lovers":                        WOWLocationData("The Maclure Vineyards",  "The Stonefield Farm",   221523_0000106),
    
}

event_location_table: Dict[str, WOWLocationData] = {
    "Become a Champion of Azeroth":                                WOWLocationData("Event", None, None)
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}


#Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set()
    location_name_groups[category].add(location)
