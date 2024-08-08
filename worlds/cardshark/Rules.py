from worlds.generic.Rules import add_rule
from .Items import trick_map

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player
    options = self.options

    for loc in location_table:
        if loc["required_tricks"]:
            if options.split_tricks:
                if loc["required_tricks"].count("Any") == 0:
                    for trick in loc["required_tricks"]:
                        pieces = trick_map[trick]
                        add_rule(multiworld.get_location(loc["name"], player),
                            lambda state, pieces=pieces: state.has_all(pieces, player))
                else:
                    combine_term = "and"
                    for trick in self.item_name_groups["viable_tricks"]:
                        pieces = trick_map[trick]
                        add_rule(multiworld.get_location(loc["name"], player),
                            lambda state, pieces=pieces: state.has_all(pieces, player), combine_term)
                        combine_term = "or"
            else:
                if loc["required_tricks"].count("Any") == 0:
                    add_rule(multiworld.get_location(loc["name"], player),
                        lambda state, loc=loc: state.has_all(loc["required_tricks"], player))
                else:
                    item_group = self.item_name_groups["viable_tricks"]
                    add_rule(multiworld.get_location(loc["name"], player),
                        lambda state, item_group=item_group: state.has_any(item_group, player))
