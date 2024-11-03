# Punkty (Numer, ID_trasy REF Trasa, Szerokość, Wysokość, Czas)
from numpy import datetime64

from Utils import *
from Data import *

def generate_next_time(start, minutes=0):
    if isinstance(start, datetime64):
        start = pd.to_datetime(start).to_pydatetime()
    next_time = start + timedelta(minutes=minutes)
    return next_time

def find_zdarzenie(id_trasy, route_data, zdarzenia_data):
    id_zdarzenia = route_data[route_data['ID'] == id_trasy]['ID_zdarzenia'].values[0]
    return zdarzenia_data[zdarzenia_data['ID'] == id_zdarzenia]


def generate_punkty(route_data, zdarzenia_data):
    # Lists for accumulating points data
    point_numbers = []
    routs_ids = []
    latitudes = []
    longitudes = []
    timestamps = []

    # Dictionary to store the start timestamps for each route
    routs_timestamps = {}

    for i in range(len(route_data)):
        if i % 1000 == 0:
            print(i)
        points_amount_in_route = random.randint(MIN_NUMBER_OF_POINTS_IN_ROUTE, MAX_NUMBER_OF_POINTS_IN_ROUTE)
        id_trasy = route_data.loc[i, 'ID']

        # Get the start timestamp for the route
        if id_trasy not in routs_timestamps:
            zdarzenie_start_time = find_zdarzenie(id_trasy, route_data, zdarzenia_data)['StartDate'].values[0]
            routs_timestamps[id_trasy] = zdarzenie_start_time
            current_timestamp = zdarzenie_start_time
        else:
            current_timestamp = routs_timestamps[id_trasy]

        # Generate random points for the route
        for j in range(points_amount_in_route):
            point_numbers.append(j)
            latitudes.append(fake.latitude())
            longitudes.append(fake.longitude())
            timestamps.append(current_timestamp)

            # Generate the next timestamp for subsequent points
            current_timestamp = generate_next_time(current_timestamp, POINT_SNAPSHOT_FREQUENCY_MIN)
            routs_ids.append(id_trasy)  # Add the route ID here

    # Create DataFrame once all data is collected
    points_data = pd.DataFrame({
        'Numer': point_numbers,
        'ID_trasy': routs_ids,
        'Szerokość': latitudes,
        'Wysokość': longitudes,
        'Czas': timestamps
    })

    return points_data
