from enum import Enum
from typing import List, TypedDict

from BaseClasses import Location

class Area(str, Enum):
    Roadside = "Roadside"
    ParkEntrance = "Park Entrance"
    StationSquare = "Station Square"
    Restroom = "Restroom"
    FairyForest = "Fairy Forest"

class LocationInfo(TypedDict):
    name: str
    id: int
    breakable: bool
    area: Area
    additionalAreas: List[Area]

base_id = 510202400

location_table: List[LocationInfo] = [
    # Roadside
    {"name": "Roadside - Among Trash",
        "id": base_id,
        "breakable": False,
        "area": Area.Roadside,
        "additionalAreas": []},
    
    # Park Entrance
    {"name": "Park Entrance - Flags Base", 
        "id": base_id + 1,
        "breakable": False,
        "area": Area.ParkEntrance,
        "additionalAreas": []},
    {"name": "Park Entrance - Trash Can",
        "id": base_id + 2,
        "breakable": False,
        "area": Area.ParkEntrance,
        "additionalAreas": []},
    
    # Station Square
    {"name": "Station Square - Light Post Base",
        "id": base_id + 3,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Gift Shop Corner",
        "id": base_id + 4,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Shack Corner",
        "id": base_id + 5,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Fence Corner",
        "id": base_id + 6,
        "breakable": False,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Glass Bottle",
        "id": base_id + 7,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Trash Can 1",
        "id": base_id + 8,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Trash Can 2",
        "id": base_id + 9,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Wooden Crate 1",
        "id": base_id + 10,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Wooden Crate 2",
        "id": base_id + 11,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    {"name": "Station Square - Vending Machine",
        "id": base_id + 12,
        "breakable": True,
        "area": Area.StationSquare,
        "additionalAreas": []},
    
    # Restroom
    {"name": "Restroom - Sink",
        "id": base_id + 13,
        "breakable": False,
        "area": Area.Restroom,
        "additionalAreas": []},

    # Fairy Forest
    {"name": "Fairy Forest - Mushroom Bushes Right",
        "id": base_id + 14,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Mushroom Bushes Left",
        "id": base_id + 15,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Back Corner",
        "id": base_id + 16,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Glass Bottle",
        "id": base_id + 17,
        "breakable": True,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Trash Can 1",
        "id": base_id + 18,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
    {"name": "Fairy Forest - Trash Can 2",
        "id": base_id + 19,
        "breakable": False,
        "area": Area.FairyForest,
        "additionalAreas": []},
]

class CrowCountryLocation(Location):
    game: str = "Crow Country"