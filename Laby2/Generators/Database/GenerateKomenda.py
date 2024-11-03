import random
from Data import *
from pandas import DataFrame

# ID int
# Adres varchar(20)
# Telefon char(9)
# Rejon varchar(15)

def generate_komendy():
    total_probability = sum(REGIONS_PROBABILITY)
    normalized_probabilities = [p / total_probability for p in REGIONS_PROBABILITY]

    chosen_regions = [random.choices(REGIONS, weights=normalized_probabilities, k=1)[0] for _ in range(NUMBER_OF_HEADQUARTERS)]

    headquarters_data = DataFrame({
        'ID': [i for i in range(NUMBER_OF_HEADQUARTERS)],
        'Address': [f"{fake.street_address()} {chosen_regions[i]}" for i in range(NUMBER_OF_HEADQUARTERS)],
        'Phone-number': [fake.phone_number() for _ in range(NUMBER_OF_HEADQUARTERS)],
        'Region': chosen_regions
    })
    return headquarters_data
