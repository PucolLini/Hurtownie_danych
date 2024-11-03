from Generators.Database.GeneratePolicjanciDanegoDnia import generate_policjanci_danego_dnia
from Generators.Database.GeneratePunkty import generate_punkty
from Generators.Database.GenerateTrasa import generate_trasy
from Generators.Database.GenerateZdarzenie import ZdarzeniaMassGenerator as zdarzeniaGenerator
from Data import *

from Generators.Database.GenerateKomenda import generate_komendy
from Generators.Database.GeneratePatrol import generate_partole
from Generators.Database.GeneratePojazdy import generate_pojazdy
from Generators.Excel.GenerateAwarie import generate_awarie
from Generators.Excel.GeneratePolicjanci import generate_policjanci
from Utils import split_dataframe, split_points_dataframe

# Komenda policji (Nazwa, Adres, Telefon, Rejon)
# Patrol (ID, Status, Data, Numer_rejestracyjny_pojazdu REF Pojazd)
# Policjant (danego dnia) (PESEL, ID_patrolu REF Patrol)
# Pojazd (Numer_rejestracyjny, Typ, Stan_techniczny, Spalanie, Rok_produkcji, Przebyte_kilometry, Marka, Model)
# Punkty (Numer, ID_trasy REF Trasa, Szerokość, Wysokość, Czas)
# Trasa (ID, ID_zdarzenia REF Zdarzenie)
# Zdarzenie (ID, DataCzas_rozpoczęcia , DataCzas_zakończenia, Lokalizacja, Opis)

##### non-changable
    # pojazdy ✓
    # komendy ✓
    # policjanci ✓

##### changable
    # awarie - stała liczba ✓
    # patrol - stała liczba ✓
    # zdarzenia - stała liczba (ale wymnożona przez dni!!) ✓
    # trasa - stała liczba (ale wymnożona przez dni!!)
    # punkty - RANDOM (ale na podstawie liczby tras?)
    # policjanci na patrolu - stała liczba ✓

if __name__ == '__main__':

    # pd_debug_setup()
    vehicle_data = generate_pojazdy()
    print(vehicle_data)
    damaged_vehicles_data = generate_awarie(vehicle_data)
    print(damaged_vehicles_data)
    headquarters_data = generate_komendy()
    print(headquarters_data)
    patrol_data = generate_partole(headquarters_data, vehicle_data)
    print(patrol_data)
    zdarzenia_data = zdarzeniaGenerator(T1_START_PERIOD_DATE, T1_END_PERIOD_DATE, ZDARZENIA_PER_DAY).generate_zdarzenia()
    print(zdarzenia_data)
    route_data = generate_trasy(zdarzenia_data, patrol_data)
    print(route_data)
    points_data = generate_punkty(route_data, zdarzenia_data)
    print(points_data)

    policemen_data = generate_policjanci()
    print(policemen_data)
    policemen_on_patrol_data = generate_policjanci_danego_dnia(patrol_data, policemen_data)
    print(policemen_on_patrol_data)

    # vehicle_data.to_csv('GeneratedOutput/Pojazd.bulk', sep='|', index=False)
    # damaged_vehicles_data.to_csv('GeneratedOutput/Awarie.bulk', sep='|', index=False)
    # headquarters_data.to_csv('GeneratedOutput/Komenda_policji.bulk', sep='|', index=False)
    # patrol_data.to_csv('GeneratedOutput/Patrol.bulk', sep='|', index=False)
    # zdarzenia_data.to_csv('GeneratedOutput/Zdarzenie.bulk', sep='|', index=False)
    # route_data.to_csv('GeneratedOutput/Trasa.bulk', sep='|', index=False)
    # points_data.to_csv('GeneratedOutput/Punkty.bulk', sep='|', index=False)
    #
    # policemen_data.to_csv('GeneratedOutput/Policjanci.bulk', sep='|', index=False)
    # policemen_on_patrol_data.to_csv('GeneratedOutput/Policjant_danego_dnia.bulk', sep='|', index=False)

######################################
##########    DZIELENIE    ###########
######################################

    t1_vehicle_data, t2_vehicle_data = split_dataframe(vehicle_data, int(NUMBER_OF_VEHICLES*2/3))
    t1_headquarters_data, t2_headquarters_data = split_dataframe(headquarters_data, int(NUMBER_OF_HEADQUARTERS*2/3))
    t1_policemen_data, t2_policemen_data = split_dataframe(policemen_data, int(NUMBER_OF_POLICEMEN*2/3))
    t1_patrol_data, t2_patrol_data = split_dataframe(patrol_data, int(NUMBER_OF_PATROLS * 2 / 3))
    t1_policemen_on_patrol_data, t2_policemen_on_patrol_data = split_dataframe(policemen_on_patrol_data, int(NUMBER_OF_POLICEMEN_ON_PATROL * 2 / 3))

    periodDateDifference = (T1_START_PERIOD_DATE - T1_END_PERIOD_DATE).days

    t1_zdarzenia_data, t2_zdarzenia_data = split_dataframe(zdarzenia_data, int(ZDARZENIA_PER_DAY * periodDateDifference * 2 / 3))
    t1_route_data, t2_route_data = split_dataframe(route_data, int(ZDARZENIA_PER_DAY * periodDateDifference * 2 / 3))
    t1_damaged_vehicles_data, t2_damaged_vehicles_data = split_dataframe(damaged_vehicles_data, int(NUMBER_OF_DAMAGES*2/3))
    t1_points_data, t2_points_data = split_points_dataframe(points_data, len(route_data))

######################################
##########  ZAPISYWANIE1   ###########
######################################

    t1_vehicle_data.to_csv('GeneratedOutput1/Pojazd.bulk', sep='|', index=False)
    t1_damaged_vehicles_data.to_csv('GeneratedOutput1/Awarie.bulk', sep='|', index=False)
    t1_headquarters_data.to_csv('GeneratedOutput1/Komenda_policji.bulk', sep='|', index=False)
    t1_patrol_data.to_csv('GeneratedOutput1/Patrol.bulk', sep='|', index=False)
    t1_zdarzenia_data.to_csv('GeneratedOutput1/Zdarzenie.bulk', sep='|', index=False)
    t1_route_data.to_csv('GeneratedOutput1/Trasa.bulk', sep='|', index=False)
    t1_points_data.to_csv('GeneratedOutput1/Punkty.bulk', sep='|', index=False)

    t1_policemen_data.to_csv('GeneratedOutput1/Policjanci.bulk', sep='|', index=False)
    t1_policemen_on_patrol_data.to_csv('GeneratedOutput1/Policjant_danego_dnia.bulk', sep='|', index=False)

######################################
##########  ZAPISYWANIE2   ###########
######################################

    t2_vehicle_data.to_csv('GeneratedOutput2/Pojazd.bulk', sep='|', index=False)
    t2_damaged_vehicles_data.to_csv('GeneratedOutput2/Awarie.bulk', sep='|', index=False)
    t2_headquarters_data.to_csv('GeneratedOutput2/Komenda_policji.bulk', sep='|', index=False)
    t2_patrol_data.to_csv('GeneratedOutput2/Patrol.bulk', sep='|', index=False)
    t2_zdarzenia_data.to_csv('GeneratedOutput2/Zdarzenie.bulk', sep='|', index=False)
    t2_route_data.to_csv('GeneratedOutput2/Trasa.bulk', sep='|', index=False)
    t2_points_data.to_csv('GeneratedOutput2/Punkty.bulk', sep='|', index=False)

    t2_policemen_data.to_csv('GeneratedOutput2/Policjanci.bulk', sep='|', index=False)
    t2_policemen_on_patrol_data.to_csv('GeneratedOutput2/Policjant_danego_dnia.bulk', sep='|', index=False)




