from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule
from .Locations import location_table

def set_rules(wowworld):
    multiworld = wowworld.multiworld
    player = wowworld.player
    options = wowworld.options
    
    # Northshire
    add_rule(wowworld.get_location("Northshire Valley - Blackrock Invasion"),
        lambda state: state.can_reach("Northshire Valley - The Rear is Clear", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Ending the Invasion"),
        lambda state: state.can_reach("Northshire Valley - Blackrock Invasion", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Extinguishing Hope"),
        lambda state: state.can_reach("Northshire Valley - The Rear is Clear", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Fear No Evil"),
        lambda state: state.can_reach("Northshire Valley - Join the Battle!", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Join the Battle!"),
        lambda state: state.can_reach("Northshire Valley - Lions for Lambs", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Lions for Lambs"),
        lambda state: state.can_reach("Northshire Valley - Beating Them Back!", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - Report to Goldshire"),
        lambda state: state.can_reach("Northshire Valley - Ending the Invasion", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - The Rear is Clear"),
        lambda state: state.can_reach("Northshire Valley - They Sent Assassins", "Location", player))
    add_rule(wowworld.get_location("Northshire Valley - The Rear is Clear"),
        lambda state: state.can_reach("Northshire Valley - Join the Battle!", "Location", player))
    
    # Elwynn Forest
    add_rule(wowworld.get_location("The Stonefield Farm - Back to Billy"),
        lambda state: state.can_reach("The Maclure Vineyards - Pie for Billy", "Location", player))
    add_rule(wowworld.get_location("Elwynn Forest - Cloth and Leather Armor"),
        lambda state: state.can_reach("Elwynn Forest - Report to Thomas", "Location", player))
    add_rule(wowworld.get_location("Lion's Pride Inn - Collecting Kelp"),
        lambda state: state.can_reach("The Stonefield Farm - Note to William", "Location", player))
    add_rule(wowworld.get_location("Goldshire - Continue to Stormwind"),
        lambda state: state.can_reach("Goldshire - A Swift Message", "Location", player))
    add_rule(wowworld.get_location("Stone Cairn Lake - Discover Rolf's Fate"),
        lambda state: state.can_reach("Elwynn Forest - Find the Lost Guards", "Location", player))
    add_rule(wowworld.get_location("Elwynn Forest - Find the Lost Guards"),
        lambda state: state.can_reach("Goldshire - Further Concerns", "Location", player))
    add_rule(wowworld.get_location("Goldshire - Further Concerns"),
        lambda state: state.can_reach("Goldshire - A Fishy Peril", "Location", player))
    add_rule(wowworld.get_location("The Maclure Vineyards - Goldtooth"),
        lambda state: state.can_reach("The Stonefield Farm - Back to Billy", "Location", player))
    add_rule(wowworld.get_location("Eastvale Logging Camp - Manhunt"),
        lambda state: state.can_reach("Eastvale Logging Camp - The Collector", "Location", player))
    add_rule(wowworld.get_location("The Stonefield Farm - Note to William"),
        lambda state: state.can_reach("The Stonefield Farm - Speak with Gramma", "Location", player))
    add_rule(wowworld.get_location("The Maclure Vineyards - Pie for Billy"),
        lambda state: state.can_reach("The Stonefield Farm - Lost Necklace", "Location", player))
    add_rule(wowworld.get_location("Elwynn Forest - Report to Thomas"),
        lambda state: state.can_reach("Stone Cairn Lake - Discover Rolf's Fate", "Location", player))
    add_rule(wowworld.get_location("The Stonefield Farm - Speak with Gramma"),
        lambda state: state.can_reach("The Maclure Vineyards - Young Lovers", "Location", player))
    add_rule(wowworld.get_location("Lion's Pride Inn - The Escape"),
        lambda state: state.can_reach("Lion's Pride Inn - Collecting Kelp", "Location", player))
    add_rule(wowworld.get_location("Goldshire - The Jasperlode Mine"),
        lambda state: state.can_reach("Goldshire - The Fargodeep Mine", "Location", player))
    add_rule(wowworld.get_location("Goldshire - The Jasperlode Mine"),
        lambda state: state.can_reach("Goldshire - The Fargodeep Mine", "Location", player))
    
    add_rule(wowworld.get_location("Become a Champion of Azeroth"),
        lambda state: state.has("Honor", player, options.honor_to_win))
    
    for name, data in location_table.items():
        add_rule(wowworld.get_location(name), lambda state, turn_in_subzone = data.quest_turn_in_category: state.has(turn_in_subzone, player))
    
    add_rule(wowworld.get_entrance("Northshire Valley"),
        lambda state: state.has("Northshire Valley", player))
    add_rule(wowworld.get_entrance("Eastvale Logging Camp"),
        lambda state: state.has("Eastvale Logging Camp", player))
    add_rule(wowworld.get_entrance("Elwynn Forest"),
        lambda state: state.has("Elwynn Forest", player))
    add_rule(wowworld.get_entrance("Forest's Edge"),
        lambda state: state.has("Forest's Edge", player))
    add_rule(wowworld.get_entrance("Goldshire"),
        lambda state: state.has("Goldshire", player))
    add_rule(wowworld.get_entrance("Lion's Pride Inn"),
        lambda state: state.has("Lion's Pride Inn", player))
    add_rule(wowworld.get_entrance("Stone Cairn Lake"),
        lambda state: state.has("Stone Cairn Lake", player))
    add_rule(wowworld.get_entrance("The Maclure Vineyards"),
        lambda state: state.has("The Maclure Vineyards", player))
    add_rule(wowworld.get_entrance("The Stonefield Farm"),
        lambda state: state.has("The Stonefield Farm", player))
    add_rule(wowworld.get_entrance("Westbrook Garrison"),
        lambda state: state.has("Westbrook Garrison", player))
    
    # Victory
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)