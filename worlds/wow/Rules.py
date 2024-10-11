from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule

def set_rules(wowworld):
    multiworld = wowworld.multiworld
    player = wowworld.player
    options = wowworld.options
    
    add_rule(wowworld.get_location("Elwynn Forest - Beating them Back!"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal McBride", player))
    add_rule(wowworld.get_location("Elwynn Forest - Lions for Lambs"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal McBride", player))
    add_rule(wowworld.get_location("Elwynn Forest - Join the Battle!"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - They Sent Assassins"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - The Rear is Clear"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Blackrock Invasion"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Extinguishing Hope"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Ending the Invasion!"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Report to Goldshire"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Fear No Evil"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Marshal McBride", player)
            and state.has("NPC: Elwynn Forest - Sergeant Willem", player)
            and state.has("NPC: Elwynn Forest - Brother Paxton", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Rest and Relaxation"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Falkhaan Isenstrider", player)
            and state.has("NPC: Elwynn Forest - Innkeeper Farley", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Gold Dust Exchange"),
        lambda state: state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player))
    add_rule(wowworld.get_location("Elwynn Forest - Kobold Candles"),
        lambda state: state.has("NPC: Elwynn Forest - William Pestle", player))
    add_rule(wowworld.get_location("Elwynn Forest - The Fargodeep Mine"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Dughan", player))
    add_rule(wowworld.get_location("Elwynn Forest - The Jasperlode Mine"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Dughan", player))
    add_rule(wowworld.get_location("Elwynn Forest - A Visit With Maybell"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Young Lovers"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
            and state.has("NPC: Elwynn Forest - Tommy Joe Stonefield", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Speak with Gramma"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
            and state.has("NPC: Elwynn Forest - Tommy Joe Stonefield", player)
            and state.has("NPC: Elwynn Forest - Gramma Stonefield", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Note to William"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
            and state.has("NPC: Elwynn Forest - Tommy Joe Stonefield", player)
            and state.has("NPC: Elwynn Forest - Gramma Stonefield", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Collecting Kelp"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
            and state.has("NPC: Elwynn Forest - Tommy Joe Stonefield", player)
            and state.has("NPC: Elwynn Forest - Gramma Stonefield", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - The Escape"),
        lambda state: (
            state.has("NPC: Elwynn Forest - William Pestle", player)
            and state.has("NPC: Elwynn Forest - Maybell Maclure", player)
            and state.has("NPC: Elwynn Forest - Tommy Joe Stonefield", player)
            and state.has("NPC: Elwynn Forest - Gramma Stonefield", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Princess Must Die!"),
        lambda state: state.has("NPC: Elwynn Forest - Ma Stonefield", player))
    add_rule(wowworld.get_location("Elwynn Forest - Lost Necklace"),
        lambda state: (
            state.has("NPC: Elwynn Forest - \"Auntie\" Bernice Stonefield", player)
            and state.has("NPC: Elwynn Forest - Billy Maclure", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Pie for Billy"),
        lambda state: (
            state.has("NPC: Elwynn Forest - \"Auntie\" Bernice Stonefield", player)
            and state.has("NPC: Elwynn Forest - Billy Maclure", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Back to Billy"),
        lambda state: (
            state.has("NPC: Elwynn Forest - \"Auntie\" Bernice Stonefield", player)
            and state.has("NPC: Elwynn Forest - Billy Maclure", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Goldtooth"),
        lambda state: (
            state.has("NPC: Elwynn Forest - \"Auntie\" Bernice Stonefield", player)
            and state.has("NPC: Elwynn Forest - Billy Maclure", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - A Fishy Peril"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Further Concerns"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
            and state.has("NPC: Elwynn Forest - Guard Thomas", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Find the Lost Guards"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
            and state.has("NPC: Elwynn Forest - Guard Thomas", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Discover Rolf's Fate"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
            and state.has("NPC: Elwynn Forest - Guard Thomas", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Report to Thomas"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
            and state.has("NPC: Elwynn Forest - Guard Thomas", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Cloth and Leather Armor"),
        lambda state: (
            state.has("NPC: Elwynn Forest - Remy \"Two Times\"", player)
            and state.has("NPC: Elwynn Forest - Marshal Dughan", player)
            and state.has("NPC: Elwynn Forest - Guard Thomas", player)
            and state.has("NPC: Elwynn Forest - Sara Timberlain", player)
        ))
    add_rule(wowworld.get_location("Elwynn Forest - Bounty on Murlocs"),
        lambda state: state.has("NPC: Elwynn Forest - Guard Thomas", player))
    add_rule(wowworld.get_location("Elwynn Forest - WANTED: James Clark"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Patterson", player))
    add_rule(wowworld.get_location("Elwynn Forest - Protect the Frontier"),
        lambda state: state.has("NPC: Elwynn Forest - Guard Thomas", player))
    add_rule(wowworld.get_location("Elwynn Forest - Fine Linen Goods"),
        lambda state: state.has("NPC: Elwynn Forest - Sara Timberlain", player))
    add_rule(wowworld.get_location("Elwynn Forest - The Collector"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Patterson", player))
    add_rule(wowworld.get_location("Elwynn Forest - Manhunt"),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Patterson", player))
    add_rule(wowworld.get_location("Elwynn Forest - Riverpaw Gnoll Bounty"),
        lambda state: state.has("NPC: Elwynn Forest - Deputy Rainer", player))
    add_rule(wowworld.get_location("Elwynn Forest - WANTED: \"Hogger\""),
        lambda state: state.has("NPC: Elwynn Forest - Marshal Dughan", player))
    
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)