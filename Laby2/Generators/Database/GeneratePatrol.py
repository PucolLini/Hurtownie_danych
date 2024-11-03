from Generators.Excel.GenerateAwarie import *
from Data import *
# ID K
# Status
# Data
# Nr rejestraycjny pojazdu FK

# DATA
def generate_partole(headquarters_data, vehicle_data):
    patrol_data = DataFrame({
        'ID': [i for i in range(NUMBER_OF_PATROLS)],
        'Status': [random.choices(STATUS, weights=PROBABILITY_OF_STATUS, k=1)[0] for _ in range(NUMBER_OF_PATROLS)],
        'Date': [rand_date(T1_START_PERIOD_DATE, T1_END_PERIOD_DATE) for _ in range(NUMBER_OF_PATROLS)],
        'Registration-number': [rand_value_from_column(column=vehicle_data['Registration-number']) for _ in range(NUMBER_OF_PATROLS)],
        'ID_komendy': [rand_value_from_column(column=headquarters_data['ID']) for _ in range(NUMBER_OF_PATROLS)]
    })
    return patrol_data
