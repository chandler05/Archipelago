from enum import Enum
from typing import List, NamedTuple, Optional, TypedDict

class TinykinType(str, Enum):
    PURPLE = "Purple"
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"

class LocInfo(NamedTuple):
    id: int
    inGameId: str
    area: str
    required_bubbles: Optional[int] = 0
    required_tinykin: Optional[List[TinykinType]] = []
    
class Location(str, Enum):
    transidor = "Transidor Crossing"
    sanctar = "City of Sanctar"
    foliana = "Foliana Heights"
    balnea_toilet = "Waters of Balnea Toilet Room"
    balnea_bath = "Waters of Balnea Bathtub Room"

base_id = 308203200

location_table = {
    "City of Sanctar - Atop Halogen Light": LocInfo(base_id + 1, "SmallLiftable_ScrewDriver", Location.sanctar, 2, [TinykinType.PURPLE]),
    "City of Sanctar - Under Couch": LocInfo(base_id + 2, "Soap_Undercouch", Location.sanctar),
    "City of Sanctar - Top of Bookshelves": LocInfo(base_id + 3, "SmallLiftable_SphinxNose", Location.sanctar, 1, [TinykinType.PURPLE, TinykinType.RED]),
    "City of Sanctar - Return Sphinx's Nose": LocInfo(base_id + 4, "Soap_Sphinx", Location.sanctar, 1, [TinykinType.PURPLE]),
    "City of Sanctar - Fix Frog": LocInfo(base_id + 5, "Soap_Guirofrog", Location.sanctar, 1, [TinykinType.PURPLE]),
    "City of Sanctar - Candles": LocInfo(base_id + 6, "Soap_Candles", Location.sanctar, 1, [TinykinType.RED]),
    "Dummy 1": LocInfo(base_id + 11, "SmallLiftable_ScrewDriver", Location.sanctar, 2, [TinykinType.PURPLE]),
    "Dummy 2": LocInfo(base_id + 12, "Soap_Undercouch", Location.sanctar),
    "Dummy 3": LocInfo(base_id + 13, "SmallLiftable_SphinxNose", Location.sanctar, 1, [TinykinType.PURPLE, TinykinType.RED]),
    "Dummy 4": LocInfo(base_id + 14, "Soap_Sphinx", Location.sanctar, 1, [TinykinType.PURPLE]),
    "Dummy 5": LocInfo(base_id + 15, "Soap_Guirofrog", Location.sanctar, 1, [TinykinType.PURPLE]),
    "Dummy 6": LocInfo(base_id + 16, "Soap_Candles", Location.sanctar, 1, [TinykinType.RED]),
    "Dummy 7": LocInfo(base_id + 17, "SmallLiftable_ScrewDriver", Location.sanctar, 2, [TinykinType.PURPLE]),
}
