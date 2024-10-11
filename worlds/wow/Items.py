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
    # Misc
    "Victory":                                            WOWItemData("VIC",       code = 221522_0000001, classification = ItemClassification.progression),
    
    # NPCs
    "NPC: Elwynn Forest - Marshal McBride":               WOWItemData("NPC",       code = 221522_1000197, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Sergeant Willem":               WOWItemData("NPC",       code = 221522_1000823, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Brother Paxton":                WOWItemData("NPC",       code = 221522_1000951, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Jorik Kerridan":                WOWItemData("NPC",       code = 221522_1000003, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Falkhaan Isenstrider":          WOWItemData("NPC",       code = 221522_1006774, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Marshal Dughan":                WOWItemData("NPC",       code = 221522_1000240, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Innkeeper Farley":              WOWItemData("NPC",       code = 221522_1000295, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Remy \"Two Times\"":            WOWItemData("NPC",       code = 221522_1000241, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - William Pestle":                WOWItemData("NPC",       code = 221522_1000253, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Maybell Maclure":               WOWItemData("NPC",       code = 221522_1000251, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Tommy Joe Stonefield":          WOWItemData("NPC",       code = 221522_1000252, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Ma Stonefield":                 WOWItemData("NPC",       code = 221522_1000244, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - \"Auntie\" Bernice Stonefield": WOWItemData("NPC",       code = 221522_1000246, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Billy Maclure":                 WOWItemData("NPC",       code = 221522_1000247, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Gramma Stonefield":             WOWItemData("NPC",       code = 221522_1000248, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Guard Thomas":                  WOWItemData("NPC",       code = 221522_1000261, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Sara Timberlain":               WOWItemData("NPC",       code = 221522_1000278, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Marshal Patterson":             WOWItemData("NPC",       code = 221522_1042256, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Supervisor Raelen":             WOWItemData("NPC",       code = 221522_1010616, classification = ItemClassification.progression),
    "NPC: Elwynn Forest - Deputy Rainer":                 WOWItemData("NPC",       code = 221522_1000963, classification = ItemClassification.progression),
    
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
    
    # Filler
    "Filler: Honor":                                      WOWItemData("Filler",    code = 221522_9000001, classification = ItemClassification.filler),
}

event_item_table: Dict[str, WOWItemData] = {}

#Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in item_table.keys():
    category = item_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
