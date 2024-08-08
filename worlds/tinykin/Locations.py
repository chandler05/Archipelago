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
    "City of Sanctar - Light Candles": LocInfo(base_id + 6, "Soap_Candles", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Find Melody": LocInfo(base_id + 7, "Artifact_Melody", Location.sanctar, 2, [TinykinType.PURPLE]),
    "City of Sanctar - Deliver Monster Picture": LocInfo(base_id + 8, "Artifact_Polaroid", Location.sanctar, 2, [TinykinType.PURPLE]),
    "City of Sanctar - Monster Picture": LocInfo(base_id + 9, "SmallLiftableBase_Picture", Location.sanctar, 1, [TinykinType.PURPLE, TinykinType.RED]),
    "City of Sanctar - TV Artifact?": LocInfo(base_id + 10, "Artifact_TV", Location.sanctar, 1, [TinykinType.PURPLE]),
    "City of Sanctar - Below Binoculars": LocInfo(base_id + 11, "SmallLiftable_PlayButton", Location.sanctar, 1, [TinykinType.PURPLE]),
    "City of Sanctar - Mail Under Couch": LocInfo(base_id + 12, "SmallLiftable_Letter_Under_Couch", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Mail Below HiFi?": LocInfo(base_id + 13, "SmallLiftable_Letter_Bellow_HiFi", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Mail Under Fragil?": LocInfo(base_id + 14, "SmallLiftable_Letter_under_Fragil", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Mail Under Piano": LocInfo(base_id + 15, "SmallLiftable_Letter_Under_Piano", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Diamond Ring?": LocInfo(base_id + 16, "SmallLiftable_Diamond", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Half Pollen?": LocInfo(base_id + 17, "?", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Full Pollen?": LocInfo(base_id + 18, "?", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Deliver All Mail": LocInfo(base_id + 19, "MasterPollen_PostOffice", Location.sanctar, 1, [TinykinType.RED]),
    "City of Sanctar - Receive Cat Door Chip": LocInfo(base_id + 20, "CatDoorChip", Location.sanctar, 1, [TinykinType.RED]),
}
