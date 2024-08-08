from logging import warning
from BaseClasses import Region
from .Locations import CrowCountryLocation

def create_regions(self):

    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)
    
    roadside = Region("Roadside", self.player, self.multiworld)
    park_entrance = Region("Park Entrance", self.player, self.multiworld)
    station_square = Region("Station Square", self.player, self.multiworld)
    restroom = Region("Restroom", self.player, self.multiworld)
    fairy_forest = Region("Fairy Forest", self.player, self.multiworld)

    for loc in self.location_name_to_id.keys():
        if self.location_name_to_area[loc] == "Roadside":
            roadside.locations.append(CrowCountryLocation(self.player, loc, self.location_name_to_id[loc], roadside))
        elif self.location_name_to_area[loc] == "Park Entrance":
            park_entrance.locations.append(CrowCountryLocation(self.player, loc, self.location_name_to_id[loc], park_entrance))
        elif self.location_name_to_area[loc] == "Station Square":
            station_square.locations.append(CrowCountryLocation(self.player, loc, self.location_name_to_id[loc], station_square))
        elif self.location_name_to_area[loc] == "Restroom":
            restroom.locations.append(CrowCountryLocation(self.player, loc, self.location_name_to_id[loc], restroom))
        elif self.location_name_to_area[loc] == "Fairy Forest":
            fairy_forest.locations.append(CrowCountryLocation(self.player, loc, self.location_name_to_id[loc], fairy_forest))
        else:
            warning(f"Location {loc} has an invalid area {self.location_name_to_area[loc]}")

    menu_region.connect(roadside)
    roadside.connect(park_entrance)
    park_entrance.connect(station_square)
    station_square.connect(restroom)
    station_square.connect(fairy_forest)

    #menu_region.connect(roadside, "Vacation Beach Main Gate", lambda state: state.has("Vacation Beach Gate Unlock", self.player))

    self.multiworld.regions.append(roadside)
    self.multiworld.regions.append(park_entrance)
    self.multiworld.regions.append(station_square)
    self.multiworld.regions.append(restroom)
    self.multiworld.regions.append(fairy_forest)
    
    #self.multiworld.completion_condition[self.player] = lambda state: (state.has_group("Gates", self.player, 3))