from BaseClasses import ItemClassification
from typing import NamedTuple

class ItemInfo(NamedTuple):
    id: int
    count: int
    classification: ItemClassification

base_id = 3021092800

item_table = {
    "Flashlight": ItemInfo(base_id, 1, ItemClassification.progression),
    "Battery": ItemInfo(base_id + 1, 133, ItemClassification.useful),
    "Hallway Key": ItemInfo(base_id + 2, 1, ItemClassification.progression),
    "Fuse": ItemInfo(base_id + 3, 8, ItemClassification.progression), # Separate each fuse from area?: Main Building, Virginia's Tape, 6 x Allen's Tape
    "Fastonyde Pill": ItemInfo(base_id + 4, 9, ItemClassification.useful),
    "Detectynol Pill": ItemInfo(base_id + 5, 9, ItemClassification.useful),
    "Vitalyxe Pill": ItemInfo(base_id + 6, 10, ItemClassification.useful),
    "Enduramyn Pill": ItemInfo(base_id + 7, 10, ItemClassification.useful),
    "Pistol Grip": ItemInfo(base_id + 5, 1, ItemClassification.progression),
    "Pistol Slide": ItemInfo(base_id + 6, 1, ItemClassification.progression),
    "Pistol Barrel": ItemInfo(base_id + 7, 1, ItemClassification.progression),
    # Pistol requires workbench to assemble. Workbench Locations: Service Hallway
    "Tape - Desmond": ItemInfo(base_id + 7, 1, ItemClassification.progression),
    "Elevator Button": ItemInfo(base_id + 8, 1, ItemClassification.progression),
    "Tape - Virginia": ItemInfo(base_id + 9, 1, ItemClassification.progression),
    "Health (1)": ItemInfo(base_id + 10, 6, ItemClassification.filler),
    "Health (5)": ItemInfo(base_id + 10, 46, ItemClassification.filler),
    "Health (10)": ItemInfo(base_id + 11, 58, ItemClassification.filler),
    "Health (15)": ItemInfo(base_id + 12, 28, ItemClassification.filler),
    "Pistol Ammo": ItemInfo(base_id + 12, 83, ItemClassification.useful), # 5 bullets
    "Mirror Shard": ItemInfo(base_id + 13, 1, ItemClassification.progression),
    "East Wing Key": ItemInfo(base_id + 14, 1, ItemClassification.progression),
    "Locker Key": ItemInfo(base_id + 15, 1, ItemClassification.progression),
    "Punch Card": ItemInfo(base_id + 16, 1, ItemClassification.progression),
    "Pen And Sticky Notes": ItemInfo(base_id + 17, 1, ItemClassification.filler), #used to put on mannequin face for fun
    "Mayer Pharmaceuticals Postcard": ItemInfo(base_id + 18, 1, ItemClassification.progression), # 0.50
    "Point Icarus Postcard": ItemInfo(base_id + 19, 1, ItemClassification.progression), # 1.00
    "Homa-Mart Postcard": ItemInfo(base_id + 20, 1, ItemClassification.progression), # 2.00
    "Elysium State Park Postcard": ItemInfo(base_id + 21, 1, ItemClassification.progression), # 1.99
    "West Wing Key": ItemInfo(base_id + 21, 1, ItemClassification.progression),
    "Brother Doll": ItemInfo(base_id + 22, 1, ItemClassification.progression),
    "Mom Doll": ItemInfo(base_id + 23, 1, ItemClassification.progression),
    "Dad Doll": ItemInfo(base_id + 24, 1, ItemClassification.progression),
    "Daughter Doll": ItemInfo(base_id + 25, 1, ItemClassification.progression),
    "Homa-Mart Coin": ItemInfo(base_id + 24, 7, ItemClassification.progression),
    "Ignition Key": ItemInfo(base_id + 25, 1, ItemClassification.progression),
    "H Block": ItemInfo(base_id + 26, 1, ItemClassification.progression),
    "A Block": ItemInfo(base_id + 27, 1, ItemClassification.progression),
    "T Block": ItemInfo(base_id + 28, 1, ItemClassification.progression),
    "E Block": ItemInfo(base_id + 29, 1, ItemClassification.progression),
    "D Block": ItemInfo(base_id + 30, 1, ItemClassification.progression),
    "Gas Mask": ItemInfo(base_id + 31, 1, ItemClassification.progression),
    "Tape - Allen": ItemInfo(base_id + 32, 1, ItemClassification.progression),
    "The Light": ItemInfo(base_id + 33, 1, ItemClassification.progression),
    "Oil Can": ItemInfo(base_id + 34, 4, ItemClassification.progression), # Each is worth 2 Oil Cans
    "Lighthouse Courtyard Key": ItemInfo(base_id + 35, 1, ItemClassification.progression),
    "Crank Wheel": ItemInfo(base_id + 36, 1, ItemClassification.progression),
    "Flare Gun": ItemInfo(base_id + 37, 1, ItemClassification.progression), # Preloaded with 3 flares
    "Flare": ItemInfo(base_id + 38, 46, ItemClassification.useful),
    "Crane Gate Key": ItemInfo(base_id + 39, 1, ItemClassification.progression),
    "TV Key": ItemInfo(base_id + 40, 1, ItemClassification.progression),
    "Buoy Key": ItemInfo(base_id + 41, 1, ItemClassification.progression),
    "Clock Key": ItemInfo(base_id + 42, 1, ItemClassification.progression),
    "Vinyl - Allen": ItemInfo(base_id + 43, 1, ItemClassification.filler),
    "Virginia's Key": ItemInfo(base_id + 44, 1, ItemClassification.progression),
    "Vinyl - Virginia": ItemInfo(base_id + 45, 1, ItemClassification.filler),
    "Shotgun": ItemInfo(base_id + 46, 1, ItemClassification.progression),
}

group_table = {
    "Dolls": ["Brother Doll", "Mom Doll", "Dad Doll", "Daughter Doll"],
    "Blocks": ["H Block", "A Block", "T Block", "E Block", "D Block"],
    "Health": ["Health (1)", "Health (5)", "Health (10)", "Health (15)"],
    "Postcards": ["Mayer Pharmaceuticals Postcard", "Point Icarus Postcard", "Homa-Mart Postcard", "Elysium State Park Postcard"],
    "Pills": ["Fastonyde Pill", "Detectynol Pill", "Vitalyxe Pill", "Enduramyn Pill"],
    "Lighthouse Keys": ["TV Key", "Buoy Key", "Clock Key"],
}