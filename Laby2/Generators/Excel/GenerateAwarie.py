import random
from pandas import DataFrame
from Utils import rand_date, rand_value_from_column
from Data import *

# Column A - Numer rejestracyjny (varchar(8))
# Column B - Uszkodzenie (enum(Silnik, Szyba, Opona, Elektronika, Zawieszenie, Skrzynia biegów, Wgniecenie, Hamulce))
# Column C - Czas (datetime)

def choose_date(start_date, end_date, vehicle_data):
    random_index = random.randint(0, NUMBER_OF_VEHICLES - 1)
    production_year = vehicle_data.loc[random_index, 'Production-year']
    production_date = datetime(year=production_year, month=1, day=1)
    chosen_date = rand_date(max(production_date, start_date), end_date)
    return chosen_date

# im pozniej tym mniej awarii? - tendencja
def generate_awarie(vehicle_data):
    damaged_vehicles = list()

    while len(damaged_vehicles) < NUMBER_OF_DAMAGES:
        damaged_vehicles.append(rand_value_from_column(column=vehicle_data['Registration-number']))

    damaged_vehicles_data = DataFrame({
        'Registration-Number': list(damaged_vehicles),
        'Damage': [random.choice(TYPES_OF_DAMAGE) for _ in range(NUMBER_OF_DAMAGES)],
        'DateTime': [choose_date(T1_START_PERIOD_DATE, T1_END_PERIOD_DATE, vehicle_data) for _ in range(NUMBER_OF_DAMAGES)]
    })
    return damaged_vehicles_data
