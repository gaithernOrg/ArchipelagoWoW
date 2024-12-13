from typing import Dict, NamedTuple, Optional, Set

from BaseClasses import Item, ItemClassification


class WOWItem(Item):
    game: str = "World of Warcraft"


class WOWItemData(NamedTuple):
    category: str
    code: int
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, WOWItemData]:
    item_dict: Dict[str, WOWItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict


item_table: Dict[str, WOWItemData] = {
    # Sub Zones
    "Northshire Valley":                                  WOWItemData("SubZone",   code = 221522_1000001, classification = ItemClassification.progression),
    "Elwynn Forest":                                      WOWItemData("SubZone",   code = 221522_1000002, classification = ItemClassification.progression),
    "Goldshire":                                          WOWItemData("SubZone",   code = 221522_1000003, classification = ItemClassification.progression),
    "Lion's Pride Inn":                                   WOWItemData("SubZone",   code = 221522_1000004, classification = ItemClassification.progression),
    "Dwarven District":                                   WOWItemData("SubZone",   code = 221522_1000005, classification = ItemClassification.progression),
    "Old Town":                                           WOWItemData("SubZone",   code = 221522_1000006, classification = ItemClassification.progression),
    "The Maclure Vineyards":                              WOWItemData("SubZone",   code = 221522_1000007, classification = ItemClassification.progression),
    "The Stonefield Farm":                                WOWItemData("SubZone",   code = 221522_1000008, classification = ItemClassification.progression),
    "Westbrook Garrison":                                 WOWItemData("SubZone",   code = 221522_1000009, classification = ItemClassification.progression),
    "Forest's Edge":                                      WOWItemData("SubZone",   code = 221522_1000010, classification = ItemClassification.progression),
    "Eastvale Logging Camp":                              WOWItemData("SubZone",   code = 221522_1000011, classification = ItemClassification.progression),
    "Stone Cairn Lake":                                   WOWItemData("SubZone",   code = 221522_1000012, classification = ItemClassification.progression),
    
    # Equipment Slot Upgrades
    "Equip Slot: Progressive Head Rarity":                WOWItemData("Equipment", code = 221522_2000001, classification = ItemClassification.progression),
    "Equip Slot: Progressive Neck Rarity":                WOWItemData("Equipment", code = 221522_2000002, classification = ItemClassification.progression),
    "Equip Slot: Progressive Shoulder Rarity":            WOWItemData("Equipment", code = 221522_2000003, classification = ItemClassification.progression),
    "Equip Slot: Progressive Shirt Rarity":               WOWItemData("Equipment", code = 221522_2000004, classification = ItemClassification.progression),
    "Equip Slot: Progressive Chest Rarity":               WOWItemData("Equipment", code = 221522_2000005, classification = ItemClassification.progression),
    "Equip Slot: Progressive Waist Rarity":               WOWItemData("Equipment", code = 221522_2000006, classification = ItemClassification.progression),
    "Equip Slot: Progressive Legs Rarity":                WOWItemData("Equipment", code = 221522_2000007, classification = ItemClassification.progression),
    "Equip Slot: Progressive Feet Rarity":                WOWItemData("Equipment", code = 221522_2000008, classification = ItemClassification.progression),
    "Equip Slot: Progressive Wrist Rarity":               WOWItemData("Equipment", code = 221522_2000009, classification = ItemClassification.progression),
    "Equip Slot: Progressive Hands Rarity":               WOWItemData("Equipment", code = 221522_2000010, classification = ItemClassification.progression),
    "Equip Slot: Progressive Finger 1 Rarity":            WOWItemData("Equipment", code = 221522_2000011, classification = ItemClassification.progression),
    "Equip Slot: Progressive Finger 2 Rarity":            WOWItemData("Equipment", code = 221522_2000012, classification = ItemClassification.progression),
    "Equip Slot: Progressive Trinket 1 Rarity":           WOWItemData("Equipment", code = 221522_2000013, classification = ItemClassification.progression),
    "Equip Slot: Progressive Trinket 2 Rarity":           WOWItemData("Equipment", code = 221522_2000014, classification = ItemClassification.progression),
    "Equip Slot: Progressive Back Rarity":                WOWItemData("Equipment", code = 221522_2000015, classification = ItemClassification.progression),
    "Equip Slot: Progressive Main Hand Rarity":           WOWItemData("Equipment", code = 221522_2000016, classification = ItemClassification.progression),
    "Equip Slot: Progressive Off Hand Rarity":            WOWItemData("Equipment", code = 221522_2000017, classification = ItemClassification.progression),
    "Equip Slot: Progressive Ranged Rarity":              WOWItemData("Equipment", code = 221522_2000018, classification = ItemClassification.progression),
    "Equip Slot: Progressive Tabard Rarity":              WOWItemData("Equipment", code = 221522_2000019, classification = ItemClassification.progression),
    
    # Misc
    "A Sense of Accomplishment":                          WOWItemData("Filler",    code = 221522_9000001, classification = ItemClassification.filler),
    "Honor":                                              WOWItemData("Macguffin", code = 221522_9000002, classification = ItemClassification.progression),
}

event_item_table: Dict[str, WOWItemData] = {
    "Victory":                                            WOWItemData("VIC",       None,                  classification = ItemClassification.progression),
}

#Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in item_table.keys():
    category = item_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
