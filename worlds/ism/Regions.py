from enum import Enum
from typing import Dict
from BaseClasses import Location, Region
from .Locations import location_table, Area
from .Rules import can_break, can_use_elevator

regions: Dict[str, Region] = {}

class Area(str, Enum):
    service_hallway = "Service Hallway"
    basement = "Basement" # Needs Hallway Key to go to and from Service Hallway
    basement_ventilations = "Basement Ventilations" # Needs Mirror Shard to enter from basement
    second_floor = "2nd Floor" # Needs fuse to use elevator
    your_home = "Your Home" # Door appears after visiting your office
    first_floor_entry = "1st Floor Entry" # Requires elevator button to go to and from 2nd floor
    first_floor = "1st Floor" # Needs mirror shard to enter from first floor entry
    virginia_apartment = "Virginia's Apartment" # First floor entry
    homa_mart = "Homa-Mart" # Needs Virginia's Tape to enter
    general_section = "Homa-Mart: General Section" # Needs Mirror Shard to enter from homa-mart entrance
    east_wing = "Homa-Mart: East Wing" # Needs East Wing Key to enter from general section
    electronics_section = "Homa-Mart: Electronics Section" # Needs Punch Card and vent breaker to enter from east wing, cannot go back through vent
    shinitzu_exhibit = "Homa-Mart: Shinitzu Exhibit" # Needs fuse and electronics room access to enter from electronics section, needs access to shinitzu exhibit and breaking tool to go to and from general section
    food_section = "Homa-Mart: Food Section" # Needs Mirror Shard to enter from homa-mart entrance, blocked by fuse on the way back so that may need to be removed
    west_wing = "Homa-Mart: West Wing" # Needs West Wing Key to enter from food section
    central_wing = "Homa-Mart: Central Wing" # Free entrance from West Wing, needs access to central wing and breaking tool to go to and from east wing, needs access to central wing and breaking tool to go to and from shinitzu exhibit
    warehouse = "Homa-Mart: Warehouse" # Needs ignition key to enter from central wing, needs breaking tool to go to and from central wing
    toy_area = "Homa-Mart: Toy Area" # Needs all four dolls to enter from shinitzu exhibit
    lobby = "Lobby" # TODO: Decide how to handle this area. Normally completing Virginia's Tape opens up a wall that leads to the lobby from the first floor, but it can also be accessed via cutting police tape at any time
    allen_home = "Allen's Home" # Needs explode barrels to enter from first floor
    reception_back_room = "Reception Back Room" # Needs explode barrels to enter from lobby
    roof = "Roof" # Needs Mirror Shard to enter from second floor
    patmos_beach = "Point Icarus: Patmos Beach" # Needs Allen's Tape to enter
    sunken_crash_site = "Point Icarus: Sunken Crash Site" # Needs breaking tool to enter from Patmos Beach
    lighthouse_parking_lot = "Point Icarus: Lighthouse Parking Lot" # Free entrance from Sunken Crash Site, can't go back that way without flare gun
    burnt_house = "Point Icarus: Burnt House" # Needs 2 fuses to enter from Lighthouse Parking Lot
    courtyard = "Point Icarus: Lighthouse Courtyard" # Needs Lighthouse Courtyard Key to enter from Lighthouse Parking Lot
    cliffs = "Point Icarus: Cliffs" # Needs 3 fuses to enter from Lighthouse Courtyard (ONE WAY)
    old_boat_house = "Point Icarus: Old Boat House" # Needs breaking tool to enter from Cliffs
    patmos_bay = "Point Icarus: Patmos Bay" # Needs crank wheel to enter from Old Boat House (ONE WAY)
    uss_thanatos = "Point Icarus: USS Thanatos" # Needs flare gun to enter from Patmos Bay
    milton_wharf = "Point Icarus: Milton Wharf" # Needs flare gun to enter from Patmos Bay
    milton_wharf_parking_lot = "Point Icarus: Milton Wharf Parking Lot" # Needs Crane Gate Key to enter from Milton Wharf
    wharf_warehouse = "Point Icarus: Warehouse" # Needs Flare Gun to enter from Milton Wharf Parking Lot (ONE WAY)
    outside_milton_wharf = "Point Icarus: Outside Milton Wharf" # Needs 3 Fuses and Warehouse access to enter from Milton Wharf (ONE WAY). Needs flare gun to go to and from Sunken Crash Site
    lighthouse = "Point Icarus: Lighthouse" # Needs Mirror Shard and Flare Gun to enter from Lighthouse Courtyard

def create_regions(self):
    regions = {area.name: Region(area.value, self.player, self.multiworld) for area in Area}
    for region in regions:
        self.multiworld.regions.append(regions[region])

    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    menu_region.connect(regions["service_hallway"])

    for loc in self.location_name_to_id.keys():
        region = self.multiworld.get_region(location_table[loc].area, self.player)
        region.locations.append(InSoundMindLocation(self.player, loc, self.location_name_to_id[loc], region))

def connect_regions(self):
    hallway_key = lambda state: state.has("Hallway Key", self.player)
    regions["service_hallway"].connect(regions["basement"], "Basement Locked Door", hallway_key)

    mirror_shard = lambda state: state.has("Mirror Shard", self.player)
    regions["basement"].connect(regions["basement_ventilations"], "Ventilation Area Entrance", mirror_shard)

    regions["basement"].connect(regions["second_floor"], "Elevator to Second Floor", lambda state: can_use_elevator(state, self.player))

    regions["second_floor"].connect(regions["your_home"])

    regions["second_floor"].connect(regions["first_floor_entry"], "Elevator to First Floor", lambda state: can_use_elevator(state, self.player) and state.has("Elevator Button", self.player))

    regions["first_floor_entry"].connect(regions["first_floor"], "First Floor Back", mirror_shard)

    regions["first_floor"].connect(regions["virginia_apartment"])

    regions["second_floor"].connect(regions["homa_mart"], "Virginia's Tape", lambda state: state.has("Tape - Virginia", self.player))

    regions["homa_mart"].connect(regions["general_section"], "General Section Tape Entrance", mirror_shard)

    east_wing_key = lambda state: state.has("East Wing Key", self.player)
    regions["general_section"].connect(regions["east_wing"], "East Wing Entrance", east_wing_key)

    regions["east_wing"].connect(regions["electronics_section"], "Electronics Section Vent", lambda state: state.has("Punch Card", self.player) and can_break(state, self.player))

    regions["electronics_section"].connect(regions["shinitzu_exhibit"], "Shinitzu Exhibit Electronics Entrance", lambda state: state.has("Fuse", self.player))  # Victoria's Fuse specifically

    regions["shinitzu_exhibit"].connect(regions["general_section"], "Shinitzu Exhibit General Entrance", lambda state: can_break(state, self.player))

    regions["food_section"].connect(regions["general_section"], "Food Section Entrance", mirror_shard)

    west_wing_key = lambda state: state.has("West Wing Key", self.player)
    regions["food_section"].connect(regions["west_wing"], "West Wing Entrance", west_wing_key)

    regions["west_wing"].connect(regions["central_wing"])
    regions["central_wing"].connect(regions["east_wing"], "Central Wing East Wing Entrance", lambda state: can_break(state, self.player))
    regions["central_wing"].connect(regions["shinitzu_exhibit"], "Central Wing Shinitzu Exhibit Entrance", lambda state: can_break(state, self.player))

    regions["central_wing"].connect(regions["warehouse"], "Warehouse Entrance", lambda state: state.has("Ignition Key", self.player))

    regions["shinitzu_exhibit"].connect(regions["toy_area"], "Toy Area Entrance", lambda state: state.has_group("Dolls", self.player, 4))

class InSoundMindLocation(Location):
    game: str = "In Sound Mind"