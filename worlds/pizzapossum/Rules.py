from worlds.generic.Rules import forbid_items_for_player, add_rule

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player
    options = self.options

    #add_rule(multiworld.get_location("Key ", player),
    #    lambda state: state.has("Toy Shovel", player))