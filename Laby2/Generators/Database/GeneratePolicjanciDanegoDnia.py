from Data import *
from Utils import *

# PESEL FK
# ID_PATROLU FK

assigned_pairs = set()

def generate_policjanci_danego_dnia(patrol_data, policemen_data):
    while len(assigned_pairs) < NUMBER_OF_POLICEMEN_ON_PATROL:
        pesel = rand_value_from_column(column=policemen_data['PESEL'])
        patrol = rand_value_from_column(column=patrol_data['ID'])

        if (pesel, patrol) not in assigned_pairs:
            assigned_pairs.add((pesel, patrol))

    policemen_on_patrol_data = pd.DataFrame(assigned_pairs, columns=['PESEL', 'ID_patrolu'])
    return policemen_on_patrol_data

