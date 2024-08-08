from typing import List, TypedDict

class LocationInfo(TypedDict):
    name: str
    id: int
    required_tricks: List[str]

base_id = 3022060200

location_table: List[LocationInfo] = [
    {"name": "Tavern - Scenario 1", "id": base_id + 1, "required_tricks": ["The Bottle of Cahors"]},
    {"name": "Cascarot Camp - Trick the Magician", "id": base_id + 2, "required_tricks": ["The Three Card Monte"]},
    {"name": "Cascarot Camp - Toss Cards in Hat (10)", "id": base_id + 3, "required_tricks": ["The Card in a Hat"]},
    {"name": "Parliament's Cafe - Scenario 1", "id": base_id + 4, "required_tricks": ["The Dishevelled Gatherer"]},
    {"name": "Parliament's Cafe - Scenario 2", "id": base_id + 5, "required_tricks": ["The Indiscreet Thief", "The Coin Flip"]},
    {"name": "Inn - Scenario 1", "id": base_id + 6, "required_tricks": ["The Indiscreet Fingers"]},
    {"name": "Inn - Scenario 2", "id": base_id + 7, "required_tricks": ["The Beginner Stack"]},
    {"name": "Manor - Scenario 1", "id": base_id + 8, "required_tricks": ["The Bottle of Bordeaux"]},
    {"name": "Manor - Scenario 2", "id": base_id + 9, "required_tricks": ["The Bottle of Burgundy"]},
    {"name": "The Barn - Scenario 1", "id": base_id + 37, "required_tricks": ["The Three Card Monte"]},
    {"name": "The Barn - Scenario 2", "id": base_id + 10, "required_tricks": ["Any"]},
    {"name": "Hospice - Scenario 1", "id": base_id + 11, "required_tricks": ["The Stolen Card"]},
    {"name": "Hospice - Scenario 2", "id": base_id + 12, "required_tricks": ["The Baby False Shuffle"]},
    {"name": "Ship - Scenario 1", "id": base_id + 13, "required_tricks": ["The Shiner"]},
    {"name": "Bandits' Den - Scenario 1", "id": base_id + 14, "required_tricks": ["The Bent Card"]},
    {"name": "Bandits' Den - Scenario 2", "id": base_id + 15, "required_tricks": ["The Stacked Shuffle", "The Duel"]},
    {"name": "Baths - Scenario 1", "id": base_id + 16, "required_tricks": ["The Oblivious Stooge", "The Card in a Hat"]},
    {"name": "Baths - Scenario 2", "id": base_id + 17, "required_tricks": ["The Stealthy Painter"]},
    {"name": "Artist's Workshop - Scenario 1", "id": base_id + 18, "required_tricks": ["The Constant Gatherer"]},
    {"name": "Gambling House - Scenario 1", "id": base_id + 19, "required_tricks": ["The Improvised Painter"]},
    {"name": "Gambling House - Scenario 2", "id": base_id + 20, "required_tricks": ["The Mirror and The Fan"]},
    {"name": "Schloss Favorite - Scenario 1", "id": base_id + 21, "required_tricks": ["The Brush and The Fan"]},
    {"name": "Cascarot Camp - Toss Cards in Hat (5)", "id": base_id + 22, "required_tricks": ["The Card in a Hat"]},
    {"name": "Cascarot Camp - Toss Cards in Hat (15)", "id": base_id + 23, "required_tricks": ["The Card in a Hat"]},
    {"name": "Cascarot Camp - Toss Cards in Hat (20)", "id": base_id + 24, "required_tricks": ["The Card in a Hat"]},
    {"name": "Cascarot Camp - Toss Cards in Hat (25)", "id": base_id + 25, "required_tricks": ["The Card in a Hat"]},
    {"name": "The Barn - Scenario 2 - 2", "id": base_id + 26, "required_tricks": ["Any"]},
    {"name": "The Barn - Scenario 2 - 3", "id": base_id + 27, "required_tricks": ["Any"]},
    {"name": "The Theatre - Scenario 1", "id": base_id + 29, "required_tricks": ["Any"]},
    {"name": "The Theatre - Scenario 1 - 2", "id": base_id + 30, "required_tricks": ["Any"]},
    {"name": "The Theatre - Scenario 1 - 3", "id": base_id + 38, "required_tricks": ["Any"]},
    {"name": "Chateau du Marais - Scenario 1", "id": base_id + 31, "required_tricks": ["The Coin Flip", "The Duel"]},
    {"name": "Chateau du Marais - Scenario 2", "id": base_id + 32, "required_tricks": ["The Bent Dealer"]},
    {"name": "Pompadour's Salon - Scenario 1", "id": base_id + 34, "required_tricks": ["The Transparent Stack", "The Duel"]},
    {"name": "Pompadour's Salon - Scenario 2", "id": base_id + 35, "required_tricks": ["The Smeared Fan"]},
    {"name": "Versailles - Scenario 1", "id": base_id + 36, "required_tricks": ["The Comte's Gambit", "The Erdnase Stack", "The Expert Dealer"]},
]
