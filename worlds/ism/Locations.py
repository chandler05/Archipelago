from enum import Enum
from typing import NamedTuple

class LocationInfo(NamedTuple):
    id: int
    inGameId: str
    area: str

base_id = 2021092800

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
    lighthouse_interior = "Point Icarus: Lighthouse Interior" # Needs Mirror Shard and Flare Gun to enter from Lighthouse Courtyard
    lighthouse = "Point Icarus: Lighthouse" # Needs 3 lighthouse keys to enter from Lighthouse Interior
    lighthouse_basement = "Point Icarus: Lighthouse Basement" # Needs The Light and some gun to enter from Lighthouse

location_table = {
    "Basement Storage Room - Shelf": LocationInfo(base_id, "", Area.service_hallway),
    "Service Hallway - Generator 1": LocationInfo(base_id + 1, "", Area.service_hallway), # Barrel needs to be exploded, or gas mask needs to be used?
    "Service Hallway - Generator 2": LocationInfo(base_id + 2, "", Area.service_hallway), # Barrel needs to be exploded, or gas mask needs to be used?
    "Work Room - Locker": LocationInfo(base_id + 1, "", Area.service_hallway), # Needs flashlight
    "Work Room - Desk": LocationInfo(base_id + 2, "", Area.service_hallway), # Needs flashlight
    "Trash Room - Vent": LocationInfo(base_id + 3, "", Area.service_hallway), # Vent needs to be broken

    "Basement Elevator Hallway - Boxes": LocationInfo(base_id + 3, "", Area.basement),
    "Basement Elevator Hallway - Chair": LocationInfo(base_id + 4, "", Area.basement),
    "Laundry Room - Fuse": LocationInfo(base_id + 5, "", Area.basement),
    "Laundry Room - Washing Machine": LocationInfo(base_id + 6, "", Area.basement),
    "Laundry Room - Locker": LocationInfo(base_id + 7, "", Area.basement),
    "Laundry Room - Behind Washing Machine": LocationInfo(base_id + 8, "", Area.basement), # Requires Fuse

    "Basement Ventilations - Utility Cart": LocationInfo(base_id + 6, "", Area.basement_ventilations),
    "Boiler Room - Locker": LocationInfo(base_id + 7, "", Area.basement_ventilations),
    "Boiler Room - Table": LocationInfo(base_id + 8, "", Area.basement_ventilations), # Boiler Room can only be left with gas mask
    
    "2nd Floor Hallway - Box 1": LocationInfo(base_id + 9, "", Area.second_floor), #10HP
    "2nd Floor Hallway - Box 2": LocationInfo(base_id + 10, "", Area.second_floor), #1HP, only appears on revisit?
    "2nd Floor Hallway - Vending Machine": LocationInfo(base_id + 9, "", Area.second_floor),
    "2nd Floor Hallway - First Corner": LocationInfo(base_id + 10, "", Area.second_floor),
    "2nd Floor Hallway - Crates": LocationInfo(base_id + 11, "", Area.second_floor),
    "2nd Floor Hallway - Last Corner": LocationInfo(base_id + 12, "", Area.second_floor),
    "2nd Floor Hallway - Utility Cart": LocationInfo(base_id + 13, "", Area.second_floor), # only appears on revisit?
    "2nd Floor Hallway - Behind Metal Sheet": LocationInfo(base_id + 14, "", Area.second_floor), #5HP
    "2nd Floor Hallway - Near Barrel": LocationInfo(base_id + 15, "", Area.second_floor), # AMMO, only appears once the gun is recieved
    "2nd Floor Hallway - Wood Palette": LocationInfo(base_id + 16, "", Area.second_floor),
    "Office - Floor": LocationInfo(base_id + 13, "", Area.second_floor), # OG Elevator Button, usually requires Desmond's Tape
    "Between Floors - Coin": LocationInfo(base_id + 14, "", Area.second_floor),

    "Desmond's Closet - Shelf 1": LocationInfo(base_id + 13, "", Area.your_home),
    "Desmond's Closet - Closet Shelf 2": LocationInfo(base_id + 14, "", Area.your_home),
    "Desmond's Kitchen - Counter": LocationInfo(base_id + 15, "", Area.your_home), #10HP
    "Desmond's Living Room - Table": LocationInfo(base_id + 15, "", Area.your_home),

    "1st Floor Storage Room - Crate 1": LocationInfo(base_id + 16, "", Area.first_floor_entry),
    "1st Floor Storage Room - Crate 2": LocationInfo(base_id + 17, "", Area.first_floor_entry),
    "1st Floor Storage Room - Crate 3": LocationInfo(base_id + 18, "", Area.first_floor_entry), #10HP
    "Utility Room - Behind Trash Can": LocationInfo(base_id + 19, "", Area.first_floor_entry), #10HP
    "Maintenance Room - Under Table": LocationInfo(base_id + 18, "", Area.first_floor_entry),
    "Maintenance Room - Table 1": LocationInfo(base_id + 19, "", Area.first_floor_entry), # Respawns?
    "Maintenance Room - Table 2": LocationInfo(base_id + 20, "", Area.first_floor_entry), # Respawns?
    "Maintenance Room - Table 3": LocationInfo(base_id + 21, "", Area.first_floor_entry), # Battery, Respawns? Same as above
    "Maintenance Room - Explosive Barrels": LocationInfo(base_id + 21, "", Area.first_floor_entry), # Needs gun to explode
    "1st Floor Hallway - Table 1": LocationInfo(base_id + 19, "", Area.first_floor_entry), #10HP
    "1st Floor Hallway - Table 2": LocationInfo(base_id + 20, "", Area.first_floor_entry), # only appears on revisit?
    "1st Floor Hallway - Table 3": LocationInfo(base_id + 21, "", Area.first_floor_entry), # Pistol Ammo, exact same as above location?
    "1st Floor Hallway - Box": LocationInfo(base_id + 21, "", Area.first_floor_entry), #15HP, only appears on revisit?
    "1st Floor Hallway - Entry Floor 1": LocationInfo(base_id + 22, "", Area.first_floor_entry), # only appears on revisit?
    "1st Floor Hallway - Entry Floor 2": LocationInfo(base_id + 22, "", Area.first_floor_entry), #15HP, only appears on revisit?
    "1st Floor Hallway - Circle Shelf": LocationInfo(base_id + 23, "", Area.first_floor_entry), # only appears on revisit?

    "1st Floor Ventilations - Chair 1": LocationInfo(base_id + 19, "", Area.first_floor),
    "1st Floor Ventilations - Chair 2": LocationInfo(base_id + 20, "", Area.first_floor), #10HP
    "1st Floor Ventilations - Electrical Box 1": LocationInfo(base_id + 21, "", Area.first_floor),
    "1st Floor Ventilations - Electrical Box 2": LocationInfo(base_id + 22, "", Area.first_floor),
    "Utility Room - Closet": LocationInfo(base_id + 23, "", Area.first_floor), # Needs Gas Mask
    "1st Floor Hallway - Hallway Floor": LocationInfo(base_id + 24, "", Area.first_floor),
    "1st Floor Closet - Locker 1": LocationInfo(base_id + 25, "", Area.first_floor),
    "1st Floor Closet - Locker 2": LocationInfo(base_id + 26, "", Area.first_floor), #15HP
    "1st Floor Ventilations - Floor 1": LocationInfo(base_id + 27, "", Area.first_floor), # Needs Flare Gun
    "1st Floor Ventilations - Floor 2": LocationInfo(base_id + 28, "", Area.first_floor), #10HP, Needs Flare Gun
    "1st Floor Ventilations - Floor 3": LocationInfo(base_id + 29, "", Area.first_floor), # Needs Flare Gun
    "1st Floor Ventilations - Floor 4": LocationInfo(base_id + 30, "", Area.first_floor), # Needs Flare Gun
    "1st Floor Ventilations - Floor 5": LocationInfo(base_id + 31, "", Area.first_floor), #10HP, Needs Flare Gun
    "1st Floor Ventilations - Floor 6": LocationInfo(base_id + 32, "", Area.first_floor), # Needs Flare Gun
    "1st Floor Ventilations - Shotgun": LocationInfo(base_id + 33, "", Area.first_floor), # Needs Flare Gun and Access to 2nd Floor Ventilations and Vent Breaker

    "Virginia's Bedroom - Desk": LocationInfo(base_id + 19, "", Area.virginia_apartment),
    "Virginia's Kitchen - Shelf": LocationInfo(base_id + 20, "", Area.virginia_apartment),
    "Virginia's Kitchen - Counter": LocationInfo(base_id + 20, "", Area.virginia_apartment), #10HP
    "Virginia's Living Room - TV Shelf": LocationInfo(base_id + 21, "", Area.virginia_apartment),
    "Virginia's Apartment - Mirror": LocationInfo(base_id + 22, "", Area.virginia_apartment), # Needs Mirror Shard
    "Virginia's Bathroom - Sink": LocationInfo(base_id + 23, "", Area.virginia_apartment), # Needs Virginia's Key

    "Between Sections - Mirror": LocationInfo(base_id + 21, "", Area.homa_mart), # Grabbing this makes impassable yellow tape appear and closes the door to the food section
    "Food Section - Table": LocationInfo(base_id + 22, "", Area.homa_mart),
    "Entrance Plaza - Circle Shelf": LocationInfo(base_id + 23, "", Area.homa_mart), # Only appears after visiting the cash registers for the first time?
    "General Section - Shelf": LocationInfo(base_id + 24, "", Area.homa_mart), # Only appears after visiting the cash registers for the first time?
    "Entrance Area - Shopping Carts": LocationInfo(base_id + 25, "", Area.homa_mart), # Needs coin to use (All 4 coins are logically needed for this)
    "Entrance Plaza - Photo Booth": LocationInfo(base_id + 26, "", Area.homa_mart), # Needs coin to use (All 4 coins are logically needed for this)

    "Between Sections - Map Table 1": LocationInfo(base_id + 23, "", Area.general_section),
    "Between Sections - Map Table 2": LocationInfo(base_id + 24, "", Area.general_section),
    "Between Sections - Map Table 3": LocationInfo(base_id + 25, "", Area.general_section),
    "General Section - Mirror": LocationInfo(base_id + 26, "", Area.general_section),
    "General Section - Corner": LocationInfo(base_id + 27, "", Area.general_section),
    "General Section - Aisle 2 (1)": LocationInfo(base_id + 27, "", Area.general_section), #10HP
    "General Section - Aisle 2 (2)": LocationInfo(base_id + 28, "", Area.general_section), #5HP
    "General Section - Aisle 2 (3)": LocationInfo(base_id + 29, "", Area.general_section), #5HP
    "General Section - Aisle 3 (1)": LocationInfo(base_id + 30, "", Area.general_section), #10HP
    "General Section - Aisle 3 (2)": LocationInfo(base_id + 31, "", Area.general_section), #5HP
    "General Section - Clearance Shelf 1": LocationInfo(base_id + 32, "", Area.general_section), #1HP
    "General Section - Clearance Shelf 2": LocationInfo(base_id + 33, "", Area.general_section), #1HP
    "Registers - Chair": LocationInfo(base_id + 34, "", Area.general_section),
    "Registers - Clearance Shelf": LocationInfo(base_id + 35, "", Area.general_section),
    "Registers - Shelf": LocationInfo(base_id + 36, "", Area.general_section), # Only appears after visiting the cash registers for the first time?
    "Registers - Register 1": LocationInfo(base_id + 37, "", Area.general_section), # Needs 2.99
    "Registers - Register 2": LocationInfo(base_id + 38, "", Area.general_section), # Needs 2.50
    "Registers - Register 3": LocationInfo(base_id + 39, "", Area.general_section), # Needs 5.00
    "Registers - Register 4": LocationInfo(base_id + 40, "", Area.general_section), # Needs 4.00

    "Manager Room - Table 1": LocationInfo(base_id + 36, "", Area.east_wing), # requires tool to break open door
    "Manager Room - Table 2": LocationInfo(base_id + 37, "", Area.east_wing), # requires tool to break open door
    "Manager Room - Safe 1": LocationInfo(base_id + 38, "", Area.east_wing), # requires tool to break open door, randomize safe code? will be incredibly difficult
    "Manager Room - Safe 2": LocationInfo(base_id + 39, "", Area.east_wing), # requires tool to break open door
    "Manager Room - Safe 3": LocationInfo(base_id + 40, "", Area.east_wing), # requires tool to break open door
    "Manager Room - Safe 4": LocationInfo(base_id + 41, "", Area.east_wing), # requires tool to break open door
    "Homa-Mart Offices - Table": LocationInfo(base_id + 38, "", Area.east_wing),
    "Staff Room - Drawer": LocationInfo(base_id + 39, "", Area.east_wing),
    "Staff Room - Cabinet": LocationInfo(base_id + 40, "", Area.east_wing), #10HP
    "Staff Room - Vending Machine": LocationInfo(base_id + 41, "", Area.east_wing), # Needs coin to use (All 4 coins are logically needed for this)
    "Maintenance East Wing - Shelf": LocationInfo(base_id + 41, "", Area.east_wing),
    "Maintenance East Wing - Floor 1": LocationInfo(base_id + 42, "", Area.east_wing),
    "Maintenance East Wing - Enemy": LocationInfo(base_id + 43, "", Area.east_wing), #MAY have been dropped by enemy, if so needs gun to kill
    "Maintenance East Wing - Box": LocationInfo(base_id + 43, "", Area.east_wing),
    "Locker Room - Locker 1": LocationInfo(base_id + 44, "", Area.east_wing), #5HP
    "Locker Room - Locker 2": LocationInfo(base_id + 45, "", Area.east_wing),
    "Locker Room - Locker 3": LocationInfo(base_id + 46, "", Area.east_wing),
    "Locker Room - Mannequin": LocationInfo(base_id + 46, "", Area.east_wing),
    "Locker Room - Locked Locker": LocationInfo(base_id + 47, "", Area.east_wing), # requires Locker Key
    "Homa-Mart Offices - Filing Cabinet": LocationInfo(base_id + 48, "", Area.east_wing),
    "Homa-Mart Offices - Mannequin": LocationInfo(base_id + 49, "", Area.east_wing),
    "Compressor Room - Boiler": LocationInfo(base_id + 50, "", Area.east_wing), # Requires Punch Card

    "Electronics Section - Table 1": LocationInfo(base_id + 51, "", Area.electronics_section), #15HP
    "Electronics Section - Table 2": LocationInfo(base_id + 52, "", Area.electronics_section),
    "Electronics Section - Table 3": LocationInfo(base_id + 53, "", Area.electronics_section),
    "Electronics Section - Shelf": LocationInfo(base_id + 54, "", Area.electronics_section), # Requires breaking tool to access from east wing entrance
    "Electronics Section - Box": LocationInfo(base_id + 55, "", Area.electronics_section), # Requires breaking tool to access from east wing entrance

    "Shinitzu Exhibit - Prize Claw": LocationInfo(base_id + 56, "", Area.shinitzu_exhibit), # Needs coin to use (All 4 coins are logically needed for this)

    "Food Section - Floor": LocationInfo(base_id + 56, "", Area.food_section),
    "Food Section - Mirror": LocationInfo(base_id + 57, "", Area.food_section),
    "Meat Section - Refrigerator 1": LocationInfo(base_id + 58, "", Area.food_section), #5HP
    "Meat Section - Refrigerator 2": LocationInfo(base_id + 59, "", Area.food_section),
    "Meat Section - Refrigerator 3": LocationInfo(base_id + 60, "", Area.food_section), #15HP
    "Deli Area - Case": LocationInfo(base_id + 61, "", Area.food_section),
    "Dairy Section - Refrigerator 1": LocationInfo(base_id + 62, "", Area.food_section), #10HP
    "Dairy Section - Refrigerator 2": LocationInfo(base_id + 63, "", Area.food_section), #10HP
    "Dairy Section - Refrigerator 3": LocationInfo(base_id + 64, "", Area.food_section), #15HP
    "Dairy Section - Refrigerator 4": LocationInfo(base_id + 65, "", Area.food_section),
    "Deli Area - Table 1": LocationInfo(base_id + 66, "", Area.food_section),
    "Deli Area - Table 2": LocationInfo(base_id + 67, "", Area.food_section), #10HP

    "Maintenance West Wing - Barrel": LocationInfo(base_id + 68, "", Area.west_wing),
    "Storage Room - Shopping Cart": LocationInfo(base_id + 69, "", Area.west_wing),
    "Maintenance West Wing - Table 1": LocationInfo(base_id + 70, "", Area.west_wing),
    "Maintenance West Wing - Table 2": LocationInfo(base_id + 71, "", Area.west_wing),
    "Freezer Room - Electrical Box 1": LocationInfo(base_id + 72, "", Area.west_wing),
    "Freezer Room - Electrical Box 2": LocationInfo(base_id + 73, "", Area.west_wing),
    "Freezer - Meat Hook": LocationInfo(base_id + 74, "", Area.west_wing), # Freezer sequence will take place, causing lock in. You'll get a key from a mannequin to escape. Do not randomize this key
    "Freezer Room - On Top of Freezer 1": LocationInfo(base_id + 75, "", Area.west_wing), #5HP, requires vent breaker to access
    "Freezer Room - On Top of Freezer 2": LocationInfo(base_id + 76, "", Area.west_wing), # Requires vent breaker to access
    "Freezer Room - On Top of Freezer 3": LocationInfo(base_id + 77, "", Area.west_wing), # Requires vent breaker to access

    "Maintenance Central Wing - Enemy": LocationInfo(base_id + 78, "", Area.central_wing), # Requires gun to kill
    "Maintenance Central Wing - Utility Cart": LocationInfo(base_id + 79, "", Area.central_wing),
    "Maintenance Central Wing - Corner": LocationInfo(base_id + 80, "", Area.central_wing),
    "Loading Bay - Utility Cart": LocationInfo(base_id + 81, "", Area.central_wing), # May be blocked by explosive barrels
    "Loading Bay - Explosive Barrels 1": LocationInfo(base_id + 82, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Explosive Barrels 2": LocationInfo(base_id + 83, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Explosive Barrels 3": LocationInfo(base_id + 84, "", Area.central_wing), #5HP, Needs gun to explode
    "Loading Bay - Explosive Barrels 4": LocationInfo(base_id + 85, "", Area.central_wing), #15HP, Needs gun to explode
    "Loading Bay - IBC": LocationInfo(base_id + 86, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Shipping Container 1": LocationInfo(base_id + 87, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Shipping Container 2": LocationInfo(base_id + 88, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Shipping Container 3": LocationInfo(base_id + 89, "", Area.central_wing), # Needs gun to explode
    "Loading Bay - Shipping Container 4": LocationInfo(base_id + 90, "", Area.central_wing), #15HP Needs gun to explode
    "Loading Bay - Shipping Container 5": LocationInfo(base_id + 91, "", Area.central_wing), #10HP Needs gun to explode
    "Loading Bay - Shelf": LocationInfo(base_id + 92, "", Area.central_wing), #5HP

    "Warehouse - Table 1": LocationInfo(base_id + 93, "", Area.warehouse),
    "Warehouse - Table 2": LocationInfo(base_id + 94, "", Area.warehouse),
    "Warehouse - Table 3": LocationInfo(base_id + 95, "", Area.warehouse),
    "Warehouse - Table 4": LocationInfo(base_id + 96, "", Area.warehouse), #15HP
    "Warehouse - Enemy": LocationInfo(base_id + 97, "", Area.warehouse), #10HP, Requires gun to kill
    "Loading Bay - Fenced Area": LocationInfo(base_id + 98, "", Area.warehouse),
    "Warehouse - Back Room Table 1": LocationInfo(base_id + 99, "", Area.warehouse),
    "Warehouse - Back Room Table 2": LocationInfo(base_id + 100, "", Area.warehouse),
    "Trash Room - Dumpster 1": LocationInfo(base_id + 101, "", Area.warehouse),
    "Trash Room - Dumpster 2": LocationInfo(base_id + 102, "", Area.warehouse),
    "Control Cabin - Pipe": LocationInfo(base_id + 103, "", Area.warehouse),
    "Control Cabin - Desk 1": LocationInfo(base_id + 104, "", Area.warehouse),
    "Control Cabin - Desk 2": LocationInfo(base_id + 105, "", Area.warehouse),
    "Control Cabin - Desk 3": LocationInfo(base_id + 106, "", Area.warehouse), #5HP

    "Toy Area - Entrance": LocationInfo(base_id + 107, "", Area.toy_area),
    "Toy Area - Entrance Floor 1": LocationInfo(base_id + 108, "", Area.toy_area),
    "Toy Area - Entrance Floor 2": LocationInfo(base_id + 109, "", Area.toy_area),
    "Toy Area - Shelf 1": LocationInfo(base_id + 110, "", Area.toy_area),
    "Toy Area - Shelf 2": LocationInfo(base_id + 111, "", Area.toy_area),
    "Toy Area - Shelf 3": LocationInfo(base_id + 112, "", Area.toy_area),
    "Toy Area - Shelf 4": LocationInfo(base_id + 113, "", Area.toy_area),
    "Toy Area - Shelf 5": LocationInfo(base_id + 114, "", Area.toy_area),
    "Toy Area - Blue Balloon": LocationInfo(base_id + 112, "", Area.toy_area),

    "Apartments - Corner": LocationInfo(base_id + 115, "", Area.lobby),
    "Apartments - Explosive Barrel": LocationInfo(base_id + 116, "", Area.lobby), # Needs gun to explode
    "Apartments - Table 1" : LocationInfo(base_id + 117, "", Area.lobby),
    "Apartments - Table 2" : LocationInfo(base_id + 118, "", Area.lobby), #5HP
    "Upper Lobby - Floor": LocationInfo(base_id + 119, "", Area.lobby), #10HP
    "1st Floor East Hallway - Table 1": LocationInfo(base_id + 120, "", Area.lobby),
    "1st Floor East Hallway - Table 2": LocationInfo(base_id + 121, "", Area.lobby), #10HP
    "Upper Lobby - Enemy": LocationInfo(base_id + 122, "", Area.lobby), #5HP, Requires gun to kill (might be random health amount?)
    "Upper Lobby - Bench": LocationInfo(base_id + 123, "", Area.lobby), #5HP
    "Upper Lobby - Side Floor": LocationInfo(base_id + 124, "", Area.lobby),
    "Upper Lobby - Side Table": LocationInfo(base_id + 125, "", Area.lobby), #5HP
    "Upper Lobby - Vending Machine 1": LocationInfo(base_id + 125, "", Area.lobby), # Needs coin to use (All 8 coins are logically needed for this)
    "Upper Lobby - Vending Machine 2": LocationInfo(base_id + 126, "", Area.lobby), # Needs coin to use (All 8 coins are logically needed for this)
    "Upper Lobby - Vending Machine 3": LocationInfo(base_id + 127, "", Area.lobby), # Needs coin to use (All 8 coins are logically needed for this)
    "Lower Lobby - Boxes 1": LocationInfo(base_id + 126, "", Area.lobby),
    "Lower Lobby - Boxes 2": LocationInfo(base_id + 127, "", Area.lobby), #5HP
    "Lower Lobby - Boxes 3": LocationInfo(base_id + 128, "", Area.lobby), #10HP
    "Lower Lobby - Ashtray": LocationInfo(base_id + 129, "", Area.lobby),
    "Lower Lobby - Enemy": LocationInfo(base_id + 130, "", Area.lobby), #5HP, Requires gun to kill

    "Allen's Kitchen - Refrigerator": LocationInfo(base_id + 113, "", Area.allen_home), #15HP
    "Allen's Kitchen - Sink": LocationInfo(base_id + 114, "", Area.allen_home), #10HP
    "Allen's Kitchen - Cabinet": LocationInfo(base_id + 115, "", Area.allen_home), #10HP
    "Allen's Kitchen - Table": LocationInfo(base_id + 116, "", Area.allen_home),
    "Allen's House - Phone Table": LocationInfo(base_id + 117, "", Area.allen_home),
    "Allen's Attic - Corner 1": LocationInfo(base_id + 118, "", Area.allen_home), # Requires flare gun to access
    "Allen's Attic - Corner 2": LocationInfo(base_id + 119, "", Area.allen_home), # Requires flare gun to access
    "Allen's Attic - Corner 3": LocationInfo(base_id + 120, "", Area.allen_home), # Requires flare gun to access
    "Allen's House Blocked Closet - Floor 1": LocationInfo(base_id + 121, "", Area.allen_home), # Requires flare gun to access
    "Allen's House Blocked Closet - Floor 2": LocationInfo(base_id + 122, "", Area.allen_home), # Requires flare gun to access
    "Allen's House Blocked Closet - Floor 3": LocationInfo(base_id + 123, "", Area.allen_home), # Requires flare gun to access
    "Allen's House Blocked Closet - Shelf 1": LocationInfo(base_id + 124, "", Area.allen_home), # Requires flare gun to access
    "Allen's House Blocked Closet - Shelf 2": LocationInfo(base_id + 125, "", Area.allen_home), # Requires flare gun to access
    "Allen's House - Circle Table": LocationInfo(base_id + 126, "", Area.allen_home), # Requires flare gun to access
    "Allen's Work Room - Desk": LocationInfo(base_id + 127, "", Area.allen_home), # Requires flare gun to access
    "Allen's Work Room - Filing Cabinet": LocationInfo(base_id + 128, "", Area.allen_home), # Requires flare gun to access
    "Allen's Bedroom - Cot": LocationInfo(base_id + 129, "", Area.allen_home), # Requires flare gun to access

    "Reception Back Room - Filing Cabinet": LocationInfo(base_id + 118, "", Area.reception_back_room), #10HP
    "Reception Back Room - Desk": LocationInfo(base_id + 119, "", Area.reception_back_room), # Flare, only appears after getting flare gun
    "Mail Room - Locker 1": LocationInfo(base_id + 119, "", Area.reception_back_room),
    "Mail Room - Locker 2": LocationInfo(base_id + 120, "", Area.reception_back_room), #10HP
    "Mail Room - Safe 1": LocationInfo(base_id + 121, "", Area.reception_back_room), # May rando safe code?
    "Mail Room - Safe 2": LocationInfo(base_id + 122, "", Area.reception_back_room), # May rando safe code?
    "Mail Room - Safe 3": LocationInfo(base_id + 123, "", Area.reception_back_room), # May rando safe code?
    "Mail Room - Safe 4": LocationInfo(base_id + 124, "", Area.reception_back_room), # May rando safe code?
    "Lower Lobby - Left Gated Area": LocationInfo(base_id + 125, "", Area.reception_back_room), # Requires vent breaker to access

    "Roof Stairs - Electrical Box 1": LocationInfo(base_id + 126, "", Area.roof),
    "Roof Stairs - Electrical Box 2": LocationInfo(base_id + 127, "", Area.roof),
    "Roof Stairs - Chair": LocationInfo(base_id + 128, "", Area.roof), #5HP
    "Roof - Boombox 1": LocationInfo(base_id + 129, "", Area.roof), #10HP
    "Roof - Boombox 2": LocationInfo(base_id + 130, "", Area.roof), #5HP
    "Roof - Vent 1": LocationInfo(base_id + 131, "", Area.roof),
    "Roof - Vent 2": LocationInfo(base_id + 132, "", Area.roof), #5HP

    "Patmos Beach - Rowboat 1": LocationInfo(base_id + 133, "", Area.patmos_beach),
    "Patmos Beach - Rowboat 2": LocationInfo(base_id + 134, "", Area.patmos_beach), #5HP
    "Patmos Beach - Rowboat 3": LocationInfo(base_id + 135, "", Area.patmos_beach), #10HP
    "Patmos Beach - Fishing Cabin": LocationInfo(base_id + 136, "", Area.patmos_beach),
    "Patmos Beach - Dock End": LocationInfo(base_id + 137, "", Area.patmos_beach),
    "Patmos Cove - Shipping Container": LocationInfo(base_id + 138, "", Area.patmos_beach), # Requires gas mask or explode barrels
    "Patmos Cove - Floating Crates 1": LocationInfo(base_id + 139, "", Area.patmos_beach),
    "Patmos Cove - Floating Crates 2": LocationInfo(base_id + 140, "", Area.patmos_beach), #5HP
    "Blocked Tunnel - Enemy 1": LocationInfo(base_id + 139, "", Area.patmos_beach), #10HP, Requires gun to kill
    "Blocked Tunnel - Enemy 2": LocationInfo(base_id + 140, "", Area.patmos_beach), #10HP, Requires gun to kill
    "Blocked Tunnel - Car Hood 1": LocationInfo(base_id + 141, "", Area.patmos_beach),
    "Blocked Tunnel - Car Hood 2": LocationInfo(base_id + 142, "", Area.patmos_beach), #5HP
    "Blocked Tunnel - Car Hood 3": LocationInfo(base_id + 143, "", Area.patmos_beach), #10HP
    "Blocked Tunnel - Car Hood 4": LocationInfo(base_id + 144, "", Area.patmos_beach), #5HP
    "Patmos Lookout - Bench 1": LocationInfo(base_id + 145, "", Area.patmos_beach), #5HP
    "Patmos Lookout - Bench 2": LocationInfo(base_id + 146, "", Area.patmos_beach), #1HP
    "Patmos Lookout - Ground": LocationInfo(base_id + 147, "", Area.patmos_beach),
    "Icarus Woods - Explosive Barrel Truck Bed 1": LocationInfo(base_id + 148, "", Area.patmos_beach), # Needs gun to explode
    "Icarus Woods - Explosive Barrel Truck Bed 2": LocationInfo(base_id + 149, "", Area.patmos_beach), #10HP, Needs gun to explode
    "Icarus Woods - Box 1": LocationInfo(base_id + 150, "", Area.patmos_beach),
    "Icarus Woods - Box 2": LocationInfo(base_id + 151, "", Area.patmos_beach),

    "Sunken Crash Site - Truck Container 1": LocationInfo(base_id + 152, "", Area.sunken_crash_site),
    "Sunken Crash Site - Truck Container 2": LocationInfo(base_id + 153, "", Area.sunken_crash_site),
    "Sunken Crash Site - Enemy 1": LocationInfo(base_id + 153, "", Area.sunken_crash_site), #5HP, Requires gun to kill
    "Sunken Crash Site - Enemy 2": LocationInfo(base_id + 154, "", Area.sunken_crash_site), #15HP, Requires gun to kill
    "Sunken Crash Site - Camp Blanket": LocationInfo(base_id + 155, "", Area.sunken_crash_site), #15HP
    "Sunken Crash Site - Camp Chair 1": LocationInfo(base_id + 156, "", Area.sunken_crash_site),
    "Sunken Crash Site - Camp Chair 2": LocationInfo(base_id + 157, "", Area.sunken_crash_site), #5HP
    "Information Center - Behind Building": LocationInfo(base_id + 158, "", Area.sunken_crash_site),
    "Information Center - Roof 1": LocationInfo(base_id + 159, "", Area.sunken_crash_site),
    "Information Center - Roof 2": LocationInfo(base_id + 160, "", Area.sunken_crash_site),
    "Information Center - Roof 3": LocationInfo(base_id + 161, "", Area.sunken_crash_site),
    "Information Center - Roof 4": LocationInfo(base_id + 162, "", Area.sunken_crash_site), #10HP
    "Information Center - Box 1": LocationInfo(base_id + 163, "", Area.sunken_crash_site),
    "Information Center - Box 2": LocationInfo(base_id + 164, "", Area.sunken_crash_site),
    "Information Center - Table 1": LocationInfo(base_id + 165, "", Area.sunken_crash_site),
    "Information Center - Table 2": LocationInfo(base_id + 166, "", Area.sunken_crash_site), #10HP
    "Icarus Lane Lookout - Bench 1": LocationInfo(base_id + 167, "", Area.sunken_crash_site), 
    "Icarus Lane Lookout - Bench 2": LocationInfo(base_id + 168, "", Area.sunken_crash_site), #5HP
    "Icarus Lane Lookout - Bench 3": LocationInfo(base_id + 169, "", Area.sunken_crash_site), #5HP
    "Icarus Lane Lookout - Bench 4": LocationInfo(base_id + 170, "", Area.sunken_crash_site), #5HP
    "Icarus Lane - Woods": LocationInfo(base_id + 171, "", Area.sunken_crash_site),
    "Icarus Lane - Truck Bed 1": LocationInfo(base_id + 172, "", Area.sunken_crash_site),
    "Icarus Lane - Truck Bed 2": LocationInfo(base_id + 173, "", Area.sunken_crash_site),
    "Icarus Lane - Truck Bed 3": LocationInfo(base_id + 174, "", Area.sunken_crash_site),
    "Lighthouse Entrance - Crate 1": LocationInfo(base_id + 175, "", Area.sunken_crash_site),
    "Lighthouse Entrance - Crate 2": LocationInfo(base_id + 176, "", Area.sunken_crash_site),
    "Lighthouse Entrance - Crate 3": LocationInfo(base_id + 177, "", Area.sunken_crash_site), #10HP
    "Icarus Lane - Darkness 1": LocationInfo(base_id + 178, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 2": LocationInfo(base_id + 179, "", Area.sunken_crash_site), #10HP, Requires Flare Gun to access
    "Icarus Lane - Darkness 3": LocationInfo(base_id + 180, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 4": LocationInfo(base_id + 181, "", Area.sunken_crash_site), #5HP, Requires Flare Gun to access
    "Icarus Lane - Darkness 5": LocationInfo(base_id + 182, "", Area.sunken_crash_site), #5HP, Requires Flare Gun to access
    "Icarus Lane - Darkness 6": LocationInfo(base_id + 183, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 7": LocationInfo(base_id + 184, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 8": LocationInfo(base_id + 185, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 9": LocationInfo(base_id + 186, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 10": LocationInfo(base_id + 187, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 11": LocationInfo(base_id + 188, "", Area.sunken_crash_site), #5HP, Requires Flare Gun to access
    "Icarus Lane - Darkness 12": LocationInfo(base_id + 189, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 13": LocationInfo(base_id + 190, "", Area.sunken_crash_site), # Requires Flare Gun to access
    "Icarus Lane - Darkness 14": LocationInfo(base_id + 191, "", Area.sunken_crash_site), #15HP, Requires Flare Gun to access

    "Outside Lighthouse - Generator": LocationInfo(base_id + 178, "", Area.lighthouse_parking_lot), #5HP
    "Outside Lighthouse - Generator Fuse": LocationInfo(base_id + 179, "", Area.lighthouse_parking_lot),
    "Outside Lighthouse - Crate Tower": LocationInfo(base_id + 180, "", Area.lighthouse_parking_lot),
    "Outside Lighthouse - Wall": LocationInfo(base_id + 181, "", Area.lighthouse_parking_lot),
    "Outside Lighthouse - Porch 1": LocationInfo(base_id + 182, "", Area.lighthouse_parking_lot),
    "Outside Lighthouse - Porch 2": LocationInfo(base_id + 183, "", Area.lighthouse_parking_lot),
    "Outside Lighthouse - Electrical Box 1": LocationInfo(base_id + 184, "", Area.lighthouse_parking_lot), # Needs breaker to access
    "Outside Lighthouse - Electrical Box 2": LocationInfo(base_id + 185, "", Area.lighthouse_parking_lot), # Needs breaker to access
    "Outside Lighthouse - Electrical Box 3": LocationInfo(base_id + 186, "", Area.lighthouse_parking_lot), #15HP, Needs breaker to access
    "Outside Lighthouse - Fuse Box": LocationInfo(base_id + 187, "", Area.lighthouse_parking_lot), # Needs breaker to access
    "Outside Lighthouse - Gated Burnt Table": LocationInfo(base_id + 188, "", Area.lighthouse_parking_lot),

    "Burnt House - Porch 1": LocationInfo(base_id + 188, "", Area.burnt_house),
    "Burnt House - Porch 2": LocationInfo(base_id + 189, "", Area.burnt_house),
    "Burnt House - Porch 3": LocationInfo(base_id + 190, "", Area.burnt_house), #15HP
    "Burnt House - Bench": LocationInfo(base_id + 191, "", Area.burnt_house),
    "Burnt House - Table 1": LocationInfo(base_id + 192, "", Area.burnt_house),
    "Burnt House - Table 2": LocationInfo(base_id + 193, "", Area.burnt_house), #5HP
    "Burnt House - Ground": LocationInfo(base_id + 194, "", Area.burnt_house), # Requires Mirror Shard to access
    "Burnt House Back Left Room - Table": LocationInfo(base_id + 195, "", Area.burnt_house), # Requires Mirror Shard and ALL Oil Can to access
    "Burnt House Back Right Room - Dresser": LocationInfo(base_id + 196, "", Area.burnt_house), # Requires Mirror Shard and ALL Oil Can to access
    "Burnt House Left Room - Box 1": LocationInfo(base_id + 197, "", Area.burnt_house), # Requires Mirror Shard and ALL Oil Can to access
    "Burnt House Left Room - Box 2": LocationInfo(base_id + 198, "", Area.burnt_house), # Requires Mirror Shard and ALL Oil Can to access
    "Burnt House - Attic": LocationInfo(base_id + 199, "", Area.burnt_house), # Requires Mirror Shard and ALL Oil Can to access

    "Lighthouse Tool Room - Table 1": LocationInfo(base_id + 200, "", Area.courtyard), #10HP
    "Lighthouse Tool Room - Table 2": LocationInfo(base_id + 201, "", Area.courtyard), #10HP
    "Lighthouse Tool Room - Shelf": LocationInfo(base_id + 202, "", Area.courtyard),
    "Courtyard - Signs": LocationInfo(base_id + 203, "", Area.courtyard),
    "Courtyard - Bench 1": LocationInfo(base_id + 204, "", Area.courtyard),
    "Courtyard - Bench 2": LocationInfo(base_id + 205, "", Area.courtyard), #5HP
    "Courtyard - Electrical Box": LocationInfo(base_id + 206, "", Area.courtyard),

    "Cliffs - Platform": LocationInfo(base_id + 207, "", Area.cliffs), #15HP
    "Cliffs - Hanging Ledge": LocationInfo(base_id + 208, "", Area.cliffs),
    "Cliffs - Behind Boat House 1": LocationInfo(base_id + 209, "", Area.cliffs),
    "Cliffs - Behind Boat House 2": LocationInfo(base_id + 210, "", Area.cliffs),

    "Old Boat House - Shelf 1": LocationInfo(base_id + 211, "", Area.old_boat_house),
    "Old Boat House - Shelf 2": LocationInfo(base_id + 212, "", Area.old_boat_house),
    "Old Boat House - Shelf 3": LocationInfo(base_id + 213, "", Area.old_boat_house),
    "Old Boat House - Shelf 4": LocationInfo(base_id + 214, "", Area.old_boat_house), # Crank Wheel needed to get back from these?
    "Old Boat House - Beam 1": LocationInfo(base_id + 215, "", Area.old_boat_house),
    "Old Boat House - Beam 2": LocationInfo(base_id + 216, "", Area.old_boat_house), #10HP
    "Old Boat House - Rowboat 1": LocationInfo(base_id + 217, "", Area.old_boat_house), #10HP
    "Old Boat House - Rowboat 2": LocationInfo(base_id + 218, "", Area.old_boat_house), #5HP

    "Patmos Bay - Crates 1": LocationInfo(base_id + 219, "", Area.patmos_bay), # Needs gun ONLY to explode
    "Patmos Bay - Crates 2": LocationInfo(base_id + 220, "", Area.patmos_bay), #15HP Needs gun ONLY to explode
    "Patmos Bay - Crates 3": LocationInfo(base_id + 221, "", Area.patmos_bay), # Needs gun ONLY to explode
    "Patmos Bay - Crates 4": LocationInfo(base_id + 222, "", Area.patmos_bay), #10HP Needs gun ONLY to explode
    "Patmos Bay - Crates 5": LocationInfo(base_id + 223, "", Area.patmos_bay), # Needs gun ONLY to explode
    "Patmos Bay - Ground": LocationInfo(base_id + 221, "", Area.patmos_bay),
    "Patmos Bay - Shipwreck 1": LocationInfo(base_id + 222, "", Area.patmos_bay),
    "Patmos Bay - Shipwreck 2": LocationInfo(base_id + 223, "", Area.patmos_bay), #15HP
    "Patmos Bay - Shipwreck 3": LocationInfo(base_id + 224, "", Area.patmos_bay), #15HP
    "Patmos Bay - Rowboat 1": LocationInfo(base_id + 225, "", Area.patmos_bay),
    "Patmos Bay - Rowboat 2": LocationInfo(base_id + 226, "", Area.patmos_bay), #5HP
    "Patmos Bay - Enemy 1": LocationInfo(base_id + 227, "", Area.patmos_bay), #10HP, Requires gun to kill
    "Patmos Bay - Enemy 2": LocationInfo(base_id + 228, "", Area.patmos_bay), #15HP, Requires gun to kill
    "Patmos Bay - Enemy 3": LocationInfo(base_id + 229, "", Area.patmos_bay), #5HP, Requires gun to kill, Only appears after visiting USS Thanatos
    "Patmos Bay - Enemy 4": LocationInfo(base_id + 230, "", Area.patmos_bay), #15HP, Requires gun to kill, Only appears after visiting USS Thanatos
    "Patmos Bay - Enemy 5": LocationInfo(base_id + 231, "", Area.patmos_bay), #5HP, Requires gun to kill, Only appears after visiting USS Thanatos
    "Patmos Bay - Enemy 6": LocationInfo(base_id + 232, "", Area.patmos_bay), #5HP, Requires gun to kill, Only appears after visiting USS Thanatos
    "Patmos Bay - Pool Under Bones": LocationInfo(base_id + 229, "", Area.patmos_bay), #10HP
    "Patmos Bay - Rocks 1": LocationInfo(base_id + 230, "", Area.patmos_bay),
    "Patmos Bay - Rocks 2": LocationInfo(base_id + 231, "", Area.patmos_bay), # Only appears after visiting USS Thanatos
    "Patmos Bay - Table 1": LocationInfo(base_id + 231, "", Area.patmos_bay),
    "Patmos Bay - Table 2": LocationInfo(base_id + 232, "", Area.patmos_bay),
    "Patmos Bay - Table 3": LocationInfo(base_id + 233, "", Area.patmos_bay),
    "Patmos Bay - Beam": LocationInfo(base_id + 234, "", Area.patmos_bay),
    "Patmos Bay - Hanging From Bones": LocationInfo(base_id + 235, "", Area.patmos_bay), # Requires Mirror Shard to access
    "USS THANATOS - Under Shipping Container": LocationInfo(base_id + 236, "", Area.patmos_bay),
    "Thanatos Interior - Flare Gun Box": LocationInfo(base_id + 237, "", Area.patmos_bay),
    "USS THANATOS - Tarp 1": LocationInfo(base_id + 238, "", Area.patmos_bay),
    "USS THANATOS - Tarp 2": LocationInfo(base_id + 239, "", Area.patmos_bay),
    "USS THANATOS - Explosive Barrel 1": LocationInfo(base_id + 240, "", Area.patmos_bay), # Needs Flare Gun to explode
    "USS THANATOS - Explosive Barrel 2": LocationInfo(base_id + 241, "", Area.patmos_bay), # Needs Flare Gun to explode
    "USS THANATOS - Shipping Container 1": LocationInfo(base_id + 242, "", Area.patmos_bay),
    "USS THANATOS - Shipping Container 2": LocationInfo(base_id + 243, "", Area.patmos_bay),
    "USS THANATOS - Shipping Container 3": LocationInfo(base_id + 244, "", Area.patmos_bay),
    "Patmos Bay - Crate Near Bones 1": LocationInfo(base_id + 245, "", Area.patmos_bay), # Needs Flare Gun to explode
    "Patmos Bay - Crate Near Bones 2": LocationInfo(base_id + 246, "", Area.patmos_bay), # Needs Flare Gun to explode
    "Patmos Bay - Shipping Container": LocationInfo(base_id + 247, "", Area.patmos_bay), # Needs Flare Gun
    "USS THANATOS - Outside Ground 1": LocationInfo(base_id + 248, "", Area.patmos_bay), #10HP
    "USS THANATOS - Outside Ground 2": LocationInfo(base_id + 249, "", Area.patmos_bay), #5HP
    "USS THANATOS - Outside Ground 3": LocationInfo(base_id + 250, "", Area.patmos_bay),

    "Thanatos Interior - Dashboard 1": LocationInfo(base_id + 238, "", Area.uss_thanatos), #15HP
    "Thanatos Interior - Dashboard 2": LocationInfo(base_id + 239, "", Area.uss_thanatos), #10HP
    "Thanatos Interior - Dashboard 3": LocationInfo(base_id + 240, "", Area.uss_thanatos),
    "Thanatos Interior - Dashboard 4": LocationInfo(base_id + 241, "", Area.uss_thanatos),
    "Thanatos Interior - Locker 1": LocationInfo(base_id + 242, "", Area.uss_thanatos), #10HP
    "Thanatos Interior - Locker 2": LocationInfo(base_id + 243, "", Area.uss_thanatos),
    "Thanatos Interior - Locker 3": LocationInfo(base_id + 244, "", Area.uss_thanatos),
    "Thanatos Exterior - Enemy 1": LocationInfo(base_id + 245, "", Area.uss_thanatos), # Pistol Ammo, Requires gun to kill

    "Milton Wharf - Left Ledge": LocationInfo(base_id + 246, "", Area.milton_wharf),
    "Milton Wharf - Right Ledge": LocationInfo(base_id + 247, "", Area.milton_wharf),
    "Milton Wharf - Hanging Shipping Container 1": LocationInfo(base_id + 247, "", Area.milton_wharf),
    "Milton Wharf - Hanging Shipping Container 2": LocationInfo(base_id + 248, "", Area.milton_wharf),
    "Milton Wharf - Hanging Shipping Container 3": LocationInfo(base_id + 249, "", Area.milton_wharf), #10HP
    "Milton Wharf - Table 1": LocationInfo(base_id + 250, "", Area.milton_wharf),
    "Milton Wharf - Table 2": LocationInfo(base_id + 251, "", Area.milton_wharf), #15HP
    "Milton Wharf - Table 3": LocationInfo(base_id + 252, "", Area.milton_wharf),
    "Milton Wharf - Table 4": LocationInfo(base_id + 253, "", Area.milton_wharf),
    "Milton Wharf - Hanging Platform": LocationInfo(base_id + 254, "", Area.milton_wharf),
    "Milton Wharf - Gated Electrical Box Right": LocationInfo(base_id + 255, "", Area.milton_wharf), # Needs access to Warehouse to access
    "Milton Wharf - Gated Electrical Box Left 1": LocationInfo(base_id + 256, "", Area.milton_wharf), # Needs access to Warehouse to access
    "Milton Wharf - Gated Electrical Box Left 2": LocationInfo(base_id + 257, "", Area.milton_wharf), #5HP, Needs access to Warehouse to access
    "Milton Wharf - Shed 1": LocationInfo(base_id + 258, "", Area.milton_wharf), # Needs access to Warehouse and Gun to explode
    "Milton Wharf - Shed 2": LocationInfo(base_id + 259, "", Area.milton_wharf), # Needs access to Warehouse and Gun to explode
    "Milton Wharf - Shed 3": LocationInfo(base_id + 260, "", Area.milton_wharf), # Needs access to Warehouse and Gun to explode
    "Milton Wharf - Shed 4": LocationInfo(base_id + 261, "", Area.milton_wharf), #10HP, Needs access to Warehouse and Gun to explode

    "Milton Wharf Parking Lot - Enemy": LocationInfo(base_id + 255, "", Area.milton_wharf_parking_lot), #Battery, Requires gun to kill
    "Milton Wharf Parking Lot - Wall 1": LocationInfo(base_id + 256, "", Area.milton_wharf_parking_lot),
    "Milton Wharf Parking Lot - Wall 2": LocationInfo(base_id + 257, "", Area.milton_wharf_parking_lot),
    "Crane - Under Stairs": LocationInfo(base_id + 258, "", Area.milton_wharf_parking_lot),
    "Crane - Dashboard": LocationInfo(base_id + 259, "", Area.milton_wharf_parking_lot), #10HP
    # "Crane - Flare Gun Box": LocationInfo(base_id + 260, "", Area.milton_wharf_parking_lot), # Infinite Flare Gun Ammo
    "Crane - Roof 1": LocationInfo(base_id + 261, "", Area.milton_wharf_parking_lot),
    "Crane - Roof 2": LocationInfo(base_id + 262, "", Area.milton_wharf_parking_lot),
    "Crane - Gated Roof": LocationInfo(base_id + 263, "", Area.milton_wharf_parking_lot),
    "Milton Wharf Parking Lot - Generator Fuse": LocationInfo(base_id + 264, "", Area.milton_wharf_parking_lot), # Requires Warehouse access
    "Milton Wharf Parking Lot - Shed Chair": LocationInfo(base_id + 265, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun
    "Milton Wharf Parking Lot - Shed Table 1": LocationInfo(base_id + 266, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun
    "Milton Wharf Parking Lot - Shed Table 2": LocationInfo(base_id + 267, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun
    "Milton Wharf Parking Lot - Shed Table 3": LocationInfo(base_id + 268, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun
    "Milton Wharf Parking Lot - Shed Table 4": LocationInfo(base_id + 269, "", Area.milton_wharf_parking_lot), #10HP, Requires Warehouse access, flare gun
    "Milton Wharf Parking Lot - Behind Shed": LocationInfo(base_id + 270, "", Area.milton_wharf_parking_lot), #5HP, Requires Warehouse access, flare gun
    "Boat Shed - Filing Cabinet": LocationInfo(base_id + 271, "", Area.milton_wharf_parking_lot), #10HP, Requires Warehouse access, flare gun, breaking tool
    "Boat Shed - Boxes 1": LocationInfo(base_id + 272, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun, breaking tool
    "Boat Shed - Boxes 2": LocationInfo(base_id + 273, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun, breaking tool
    "Boat Shed - Boxes 3": LocationInfo(base_id + 274, "", Area.milton_wharf_parking_lot), #5HP, Requires Warehouse access, flare gun, breaking tool
    "Boat Shed - Fuse Box": LocationInfo(base_id + 275, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun, breaking tool
    "Behind Boat Shed - Electrical Box": LocationInfo(base_id + 276, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun, breaking tool
    "Milton Wharf Parking Lot - Gated Electrical Box 1": LocationInfo(base_id + 277, "", Area.milton_wharf_parking_lot), #10HP, Requires Warehouse access, flare gun, breaking tool
    "Milton Wharf Parking Lot - Gated Electrical Box 2": LocationInfo(base_id + 278, "", Area.milton_wharf_parking_lot), # Requires Warehouse access, flare gun, breaking tool
    "Milton Wharf Parking Lot - Shipping Crate Tower": LocationInfo(base_id + 279, "", Area.milton_wharf_parking_lot), # Requires Warehouse access

    "Warehouse Roof - Crates 1": LocationInfo(base_id + 264, "", Area.wharf_warehouse), # Needs Flare Gun to explode
    "Warehouse Roof - Crates 2": LocationInfo(base_id + 265, "", Area.wharf_warehouse), # Needs Flare Gun to explode
    "Warehouse Roof - Crates 3": LocationInfo(base_id + 266, "", Area.wharf_warehouse), # Needs Flare Gun to explode 
    "Warehouse Roof - Crates 4": LocationInfo(base_id + 267, "", Area.wharf_warehouse), # Needs Flare Gun to explode
    "Warehouse Roof - Crates 5": LocationInfo(base_id + 268, "", Area.wharf_warehouse), #10HP, Needs Flare Gun to explode
    "Warehouse Entrance - Shelf 1": LocationInfo(base_id + 269, "", Area.wharf_warehouse),
    "Warehouse Entrance - Shelf 2": LocationInfo(base_id + 270, "", Area.wharf_warehouse), #15HP
    "Warehouse Entrance - Shelf 3": LocationInfo(base_id + 271, "", Area.wharf_warehouse),
    "Warehouse Entrance - Shelf 4": LocationInfo(base_id + 272, "", Area.wharf_warehouse), #10HP
    "Warehouse Entrance - Shelf 5": LocationInfo(base_id + 273, "", Area.wharf_warehouse),
    "Warehouse Entrance - Shelf 6": LocationInfo(base_id + 274, "", Area.wharf_warehouse), #10HP
    "Warehouse Entrance - Shelf 7": LocationInfo(base_id + 275, "", Area.wharf_warehouse),
    "Warehouse - Dead End Shelf": LocationInfo(base_id + 276, "", Area.wharf_warehouse),
    "Warehouse - Corner Shelf": LocationInfo(base_id + 277, "", Area.wharf_warehouse),
    "Warehouse - Shelf 1": LocationInfo(base_id + 277, "", Area.wharf_warehouse),
    "Warehouse - Shelf 2": LocationInfo(base_id + 278, "", Area.wharf_warehouse),
    "Warehouse - Shelf 3": LocationInfo(base_id + 279, "", Area.wharf_warehouse),
    "Warehouse - Shelf 4": LocationInfo(base_id + 280, "", Area.wharf_warehouse),
    "Warehouse - Concrete Platform 1": LocationInfo(base_id + 281, "", Area.wharf_warehouse),
    "Warehouse - Concrete Platform 2": LocationInfo(base_id + 282, "", Area.wharf_warehouse),
    "Warehouse - Concrete Platform 3": LocationInfo(base_id + 283, "", Area.wharf_warehouse), #15HP
    "Control Room - Filing Cabinet": LocationInfo(base_id + 284, "", Area.wharf_warehouse),
    "Control Room - Desk 1": LocationInfo(base_id + 285, "", Area.wharf_warehouse),
    "Control Room - Desk 2": LocationInfo(base_id + 286, "", Area.wharf_warehouse),
    "Control Room - Desk 3": LocationInfo(base_id + 287, "", Area.wharf_warehouse), #5HP

    "Security Checkpoint - Shelf 1": LocationInfo(base_id + 288, "", Area.outside_milton_wharf), #5HP
    "Security Checkpoint - Shelf 2": LocationInfo(base_id + 289, "", Area.outside_milton_wharf),
    "Security Checkpoint - Shelf 3": LocationInfo(base_id + 290, "", Area.outside_milton_wharf),
    "Security Checkpoint - Shelf 4": LocationInfo(base_id + 291, "", Area.outside_milton_wharf), #15HP
    "Security Checkpoint - Shelf 5": LocationInfo(base_id + 292, "", Area.outside_milton_wharf),
    "Security Checkpoint - Shelf 6": LocationInfo(base_id + 293, "", Area.outside_milton_wharf),
    "Security Checkpoint - Shelf 7": LocationInfo(base_id + 294, "", Area.outside_milton_wharf), #1HP
    "Exit Tunnel - Tracks": LocationInfo(base_id + 295, "", Area.outside_milton_wharf),
    "Road Checkpoint 2 - Ground": LocationInfo(base_id + 296, "", Area.outside_milton_wharf),
    "Road Checkpoint 2 - Tarps 1": LocationInfo(base_id + 297, "", Area.outside_milton_wharf),
    "Road Checkpoint 2 - Tarps 2": LocationInfo(base_id + 298, "", Area.outside_milton_wharf),

    "Lighthouse Living Room - Table": LocationInfo(base_id + 299, "", Area.lighthouse_interior),
    "Lighthouse Living Room - TV Key": LocationInfo(base_id + 300, "", Area.lighthouse_interior),
    "Lighthouse Kitchen - Shelf": LocationInfo(base_id + 301, "", Area.lighthouse_interior),
    "Lighthouse Kitchen - Refrigerator": LocationInfo(base_id + 302, "", Area.lighthouse_interior), #10HP
    "Lighthouse Kitchen - Cupboard": LocationInfo(base_id + 303, "", Area.lighthouse_interior), #10HP
    "Lighthouse Bedroom - Shelf": LocationInfo(base_id + 304, "", Area.lighthouse_interior),
    "Lighthouse Bedroom - Clock Key": LocationInfo(base_id + 305, "", Area.lighthouse_interior),
    "Lighthouse Closet - Shelf": LocationInfo(base_id + 305, "", Area.lighthouse_interior),
    "Lighthouse Closet - Buoy Key": LocationInfo(base_id + 306, "", Area.lighthouse_interior),
    "Lighthouse Interior - Drawer": LocationInfo(base_id + 307, "", Area.lighthouse_interior), #5HP

    "Lighthouse Stairwell - Table 1": LocationInfo(base_id + 308, "", Area.lighthouse), #10HP
    "Lighthouse Stairwell - Table 2": LocationInfo(base_id + 309, "", Area.lighthouse), #5HP
    "Lighthouse Stairwell - Table 3": LocationInfo(base_id + 310, "", Area.lighthouse),
    "Lighthouse Stairwell - Shelf": LocationInfo(base_id + 311, "", Area.lighthouse),
    "Lighthouse Top - Walkway 1": LocationInfo(base_id + 312, "", Area.lighthouse),
    "Lighthouse Top - Walkway 2": LocationInfo(base_id + 313, "", Area.lighthouse),
    "Lighthouse Top - Walkway 3": LocationInfo(base_id + 314, "", Area.lighthouse),
    "Lighthouse Top - Walkway 4": LocationInfo(base_id + 315, "", Area.lighthouse),
    "Lighthouse Top - Walkway 5": LocationInfo(base_id + 316, "", Area.lighthouse),
    "Lighthouse Top - Walkway 6": LocationInfo(base_id + 317, "", Area.lighthouse),
    "Lighthouse Top - Walkway 7": LocationInfo(base_id + 318, "", Area.lighthouse),

    "Lighthouse Basement - Chair": LocationInfo(base_id + 319, "", Area.lighthouse_basement), #10HP
    "Lighthouse Basement - Table 1": LocationInfo(base_id + 320, "", Area.lighthouse_basement), #10HP
    "Lighthouse Basement - Table 2": LocationInfo(base_id + 321, "", Area.lighthouse_basement), #10HP
    "Lighthouse Basement - Table 3": LocationInfo(base_id + 322, "", Area.lighthouse_basement),
    "Lighthouse Basement - Table 4": LocationInfo(base_id + 323, "", Area.lighthouse_basement),
    "Lighthouse Basement - Table 5": LocationInfo(base_id + 324, "", Area.lighthouse_basement),
    "Generator Room - Corner": LocationInfo(base_id + 325, "", Area.lighthouse_basement), #15HP
    "Generator Room - Behind Generator": LocationInfo(base_id + 326, "", Area.lighthouse_basement),
    "Generator Room - Back Floor Left": LocationInfo(base_id + 327, "", Area.lighthouse_basement),
    "Generator Room - Back Floor Right": LocationInfo(base_id + 328, "", Area.lighthouse_basement),
    "Generator Room - Generator Corner 1": LocationInfo(base_id + 329, "", Area.lighthouse_basement),
    "Generator Room - Generator Corner 2": LocationInfo(base_id + 330, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Right 1": LocationInfo(base_id + 331, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Right 2": LocationInfo(base_id + 332, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Right 3": LocationInfo(base_id + 333, "", Area.lighthouse_basement), #15HP
    "Generator Room - Random Flare": LocationInfo(base_id + 334, "", Area.lighthouse_basement), # Randomly appears after activating generator
    "Generator Room - Blocked Area Left 1": LocationInfo(base_id + 335, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Left 2": LocationInfo(base_id + 336, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Left 3": LocationInfo(base_id + 337, "", Area.lighthouse_basement),
    "Generator Room - Blocked Area Left 4": LocationInfo(base_id + 338, "", Area.lighthouse_basement), #5HP
}
