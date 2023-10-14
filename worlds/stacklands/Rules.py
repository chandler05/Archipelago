from worlds.generic.Rules import set_rule, add_rule

def create_rules(self, location_table):
    world = self.multiworld
    player = self.player

    set_rule(world.get_location("Have 5 Ideas", self.player),
        lambda state: state.count_group("Mainland Ideas", player) >= 5)
    set_rule(world.get_location("Have 10 Ideas", self.player),
        lambda state: state.count_group("Mainland Ideas", player) >= 10)
    
    set_rule(world.get_location("Unlock All Packs", self.player),
        lambda state: state.has_group("Mainland Booster Packs", player, 8))

    for loc in location_table:
        if len(loc["potentialBoosterPacks"]) > 0:
            add_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_any(set(loc["potentialBoosterPacks"]), player))
        if loc["requireBasicPacks"]:
            add_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_group("Basic Mainland Booster Packs", player))
        if len(loc["ideas"]) > 0:
            add_rule(world.get_location(loc["name"], self.player),
                lambda state: state.has_all(set(loc["ideas"]), player))