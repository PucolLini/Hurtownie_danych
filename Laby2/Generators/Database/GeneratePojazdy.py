import random
import string
from Data import *
from pandas import DataFrame

# Numer_rejestracyjny K
# Typ
# Stan_techniczny
# Spalanie
# Rok_produkcji
# Przebyte_kilometry
# Marka
# Model

def generate_registration_number():
    registration_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ' ' + \
                          ''.join(random.choices(string.digits, k=4))
    return registration_number

def correct_helicopters_data(vehicle_data):
    for i in range(NUMBER_OF_VEHICLES):
        if vehicle_data['Type'][i] == 'Helikopter':
            vehicle_data['Combustion'][i] = round(random.uniform(20.0, 100.0), 2)
            selected_brand = random.choice(list(HELICOPTER_BRANDS.keys()))
            vehicle_data['Brand'][i] = selected_brand
            vehicle_data['Model'][i] = random.choice(HELICOPTER_BRANDS[selected_brand])

def generate_pojazdy():
    registration_numbers = set()
    while len(registration_numbers) < NUMBER_OF_VEHICLES:
        registration_numbers.add(generate_registration_number())

    list_of_models = list()
    list_of_brands = list()
    for i in range(NUMBER_OF_VEHICLES):
        brand = random.choice(list(BRANDS.keys()))
        model = random.choice(BRANDS[brand])
        list_of_brands.append(brand)
        list_of_models.append(model)

    vehicle_data = {
        'Registration-number': list(registration_numbers),
        'Type': [random.choice(TYPES) for _ in range(NUMBER_OF_VEHICLES)],
        'Technical-condition': [random.choices(CONDITION, weights=PROBABILITY, k=1)[0] for _ in range(NUMBER_OF_VEHICLES)],
        'Combustion': [round(random.uniform(4.0, 15.0), 2) for _ in range(NUMBER_OF_VEHICLES)],
        'Production-year': [random.randint(2000, 2018) for _ in range(NUMBER_OF_VEHICLES)],
        'Kilometers-traveled': [random.randint(0, 200000) for _ in range(NUMBER_OF_VEHICLES)],
        'Brand': list(list_of_brands),
        'Model': list(list_of_models)
    }

    correct_helicopters_data(vehicle_data)
    vehicle_data = DataFrame(vehicle_data)
    return vehicle_data
