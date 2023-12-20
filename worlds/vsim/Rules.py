from worlds.generic.Rules import add_rule

def create_rules(self, location_table):
    multiworld = self.multiworld
    player = self.player
    options = self.options

    for loc in location_table:
        if loc["needsCamera"]:
            add_rule(multiworld.get_location(loc["name"], player),
                lambda state: state.has("Camera", player))
        if len(loc["additionalAreas"]) > 0:
            for area in loc["additionalAreas"]:
                add_rule(multiworld.get_location(loc["name"], player),
                    lambda state, x=area: state.can_reach(multiworld.get_region(x, player), player))

    chain_locations(self, [
        "Vacation Beach - Beach Orders I",
        "Vacation Beach - Beach Orders II",
        "Vacation Beach - Beach Orders III",
        "Vacation Beach - Beach Orders IV",
    ])
    chain_locations(self, [
        "Vacation Beach - Beach Photos I",
        "Vacation Beach - Beach Photos II",
        "Vacation Beach - Beach Photos III",
        "Vacation Beach - Beach Photos IV",
    ])

    chain_locations(self, [
        "Vacation Forest - Forest Orders I",
        "Vacation Forest - Forest Orders II",
        "Vacation Forest - Forest Orders III",
        "Vacation Forest - Forest Orders IV",
    ])
    chain_locations(self, [
        "Vacation Forest - Forest Photos I",
        "Vacation Forest - Forest Photos II",
        "Vacation Forest - Forest Photos III",
        "Vacation Forest - Forest Photos IV",
    ])
    chain_locations(self, [
        "Vacation Forest - Forest Targets",
        "Vacation Forest - Beach Targets",
        "Vacation Forest - Mountain Targets",
    ])

    chain_locations(self, [
        "Vacation Mountain - Mountain Orders I",
        "Vacation Mountain - Mountain Orders II",
        "Vacation Mountain - Mountain Orders III",
        "Vacation Mountain - Mountain Orders IV",
    ])
    chain_locations(self, [
        "Vacation Mountain - Mountain Photos I",
        "Vacation Mountain - Mountain Photos II",
        "Vacation Mountain - Mountain Photos III",
        "Vacation Mountain - Mountain Photos IV",
    ])

def chain_locations(self, locations):
    multiworld = self.multiworld
    player = self.player

    for i in range(len(locations)):
        if i == 0:
            continue
        add_rule(multiworld.get_location(locations[i], player),
            lambda state, x=i: state.can_reach(multiworld.get_location(locations[x-1], player), player))