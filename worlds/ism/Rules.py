from worlds.generic.Rules import forbid_items_for_player, add_rule
from .Locations import Area

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player
    options = self.options

    #add_rule(multiworld.get_location("Beachstickball (10 Hits)", player),
    #    lambda state: state.has("Stick", player))

def can_break(state, player) -> bool:
    return state.has("Mirror Shard", player) or can_assemble_pistol(state, player) or state.has("Flare Gun", player) or state.has("Shotgun", player)

def can_assemble_pistol(state, player) -> bool:
    return (state.has("Pistol Grip", player) 
        and state.has("Pistol Slide", player)
        and state.has("Pistol Barrel", player)
        and can_use_workbench(state, player))

def can_use_workbench(state, player) -> bool:
    return state.can_reach("Service Hallway", "Region", player) and state.has("Flashlight", player)

def completed_victoria_tape(state, player) -> bool:
    return (state.can_reach("Between Sections - Mirror", "Location", player)
        and state.can_reach("General Section - Mirror", "Location", player)
        and state.can_reach("Food Section - Mirror", "Location", player)
        and state.can_reach(Area.electronics_section, "Region", player)
        and state.has("Fuse", player) # Victoria's Fuse specifically
        and state.can_reach(Area.toy_area, "Region", player)
        and state.has_group("Blocks", player, 5))

def can_pass_chemical_with_barrel(state, player) -> bool:
    return can_assemble_pistol(state, player) or state.has("Gas Mask", player) or state.has("Flare Gun", player) or state.has("Shotgun", player) # Add explosive pills when implemented

def can_explode_barrels(state, player) -> bool:
    return can_assemble_pistol(state, player) or state.has("Flare Gun", player) or state.has("Shotgun", player)

# def can_explode_chemical(state, player) -> bool:
#     return # Add explosive pills when implemented

def can_cut_tape(state, player) -> bool:
    return state.has("Mirror Shard", player)

def can_use_elevator(state, player) -> bool:
    return state.has("Fuse", player) and state.can_reach(Area.basement, "Region", player)

def shadow_in_wharf(state, player) -> bool:
    return state.can_reach(Area.wharf_warehouse, "Region", player)