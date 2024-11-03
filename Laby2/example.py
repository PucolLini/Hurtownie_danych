# This is a sample Python script.
import random
import string
from datetime import date, datetime, timedelta
import pandas as pd
from faker import Faker
import numpy as np


def generate_pesel():
    birth_date = date.fromordinal(random.randint(date(1954, 1, 1).toordinal(), date(2006, 12, 31).toordinal()))
    year = birth_date.year % 100  # the rest from division by 100
    month = birth_date.month
    day = birth_date.day

    if birth_date.year >= 2000:
        month += 20

    random_digits = [random.randint(0, 9) for _ in range(4)]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(w * d for w, d in
                      zip(weights, [int(d) for d in f"{year:02}{month:02}{day:02}{''.join(map(str, random_digits))}"]))
    control_digit = (10 - (control_sum % 10)) % 10

    pesel = f"{year:02}{month:02}{day:02}{''.join(map(str, random_digits))}{control_digit}"

    return pesel


def generate_phone_number():
    phone_digits = [random.randint(0, 9) for _ in range(9)]
    phone_number = ''.join(map(str, phone_digits))
    return phone_number


def generate_license_number():
    characters = string.ascii_uppercase + string.digits
    license_number = ''.join(random.choices(characters, k=10))
    return license_number


def generate_registration_number():
    registration_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ' ' + \
                          ''.join(random.choices( string.digits, k=4))
    return registration_number


def generate_renting_number():
    characters = string.ascii_uppercase + string.digits
    renting_nr = ''.join(random.choices(characters, k=12))
    return renting_nr


def generate_tackle_with_C():
    tackles = ['not available cars', 'not transparent pricing', 'verification process', 'not clear insurance coverage']
    return random.choices(tackles)


def generate_source_of_finding_out_G():
    sources = ['friends', 'web', 'advertisement in Internet', 'our cars in city', 'billboards']
    return random.choices(sources)


# CLIENT
fake = Faker()
client_number = 1600
client_t1 = 1000
client_t2 = client_number - client_t1
unique_pesel = set()
while len(unique_pesel) < client_number:
    unique_pesel.add(generate_pesel())
lic_num = set()
while len(lic_num) < client_number:
    lic_num.add(generate_license_number())
p_num = set()
while len(p_num) < client_number:
    p_num.add(generate_phone_number())
clients_dataframe = {
    'PESEL': list(unique_pesel),
    'name': [fake.first_name() for _ in range(client_number)],
    'surname': [fake.last_name() for _ in range(client_number)],
    'address': [fake.address().replace('\n', ' ').replace(',', ' ') for _ in range(client_number)],
    'phone number': list(p_num),
    'licence number': list(lic_num)
}
clients_dataframe = pd.DataFrame(clients_dataframe)
domains = ['@gmail.com', '@outlook.com', '@icloud.com', '@wp.pl', '@onet.pl']
clients_dataframe['e-mail'] = clients_dataframe['name'].str.lower() + '.' + clients_dataframe['surname'].str.lower() + random.choices(domains)
# print(clients_dataframe)
clients_df_t1 = clients_dataframe.head(client_t1)
clients_df_t2 = clients_dataframe.iloc[client_t1:client_number]

# CAR
models = ['Clio', 'Sandero', 'Arkana', 'Mazda2', 'Express', 'Dokker', 'Master']
brands = {'Clio': 'RENAULT', 'Sandero': 'DACIA', 'Arkana': 'RENAULT', 'Mazda2': 'MAZDA', 'Express': 'RENAULT', 'Dokker': 'DACIA', 'Master': 'RENAULT'}
types = {'Clio': 'Passenger car', 'Sandero': 'Passenger car', 'Arkana': 'Passenger car', 'Mazda2': 'Passenger car', 'Express': 'Delivery car', 'Dokker': 'Delivery car', 'Master': 'Delivery car'}
fuel = {'Clio': 'Petrol', 'Sandero': 'Petrol', 'Arkana': 'Petrol', 'Mazda2': 'Hybrid', 'Express': 'Petrol', 'Dokker': 'Petrol', 'Master': 'Diesel'}
cars_number = 130
cars_t1 = 100
cars_t2 = cars_number - cars_t1
unique_car = set()
while len(unique_car) < cars_number:
    unique_car.add(generate_registration_number())


cars_dataframe = {
    'Registration number': list(unique_car),
    'Drivable': [random.randint(0, 1) for _ in range(cars_number)],
    'Model': [random.choice(models) for _ in range(cars_number)]
}
cars_dataframe = pd.DataFrame(cars_dataframe)
cars_dataframe['Brand'] = cars_dataframe['Model'].map(brands)
cars_dataframe['Type'] = cars_dataframe['Model'].map(types)
cars_dataframe['Fuel'] = cars_dataframe['Model'].map(fuel)

cars_df_t1 = cars_dataframe.head(cars_t1)
cars_df_t2 = cars_dataframe.iloc[cars_t1:cars_number]

# CAR INFO
car_info_number = 50000
car_info_t1 = 20000
car_info_t2 = car_info_number - car_info_t1
bad_working = [' ', ' ', ' ', 'engine', 'gearbox', 'windshield wipers', ' ', 'clutch']
damages = [' ', ' ', ' ', 'no mirror', 'dent', 'scratch', ' ', ' ', 'flat tyre']
car_info_df = {
    'is clean': [random.randint(0, 1) for _ in range(car_info_number)],
    'is damage': [random.randint(0, 1) for _ in range(car_info_number)],
    'damages': [random.choices(damages) for _ in range(car_info_number)],
    'is sth working bad': [random.randint(0, 1) for _ in range(car_info_number)],
    'bad working things': [random.choices(bad_working) for _ in range(car_info_number)],
    'month': [random.randint(1, 12) for _ in range(car_info_number)]
}
car_info_df = pd.DataFrame(car_info_df)
car_info_df['CarInfoNumber'] = car_info_df.index + 1

random_cars_t1 = cars_df_t1['Registration number'].sample(n=car_info_t1, replace=True).reset_index(drop=True)
random_cars_t2 = cars_dataframe['Registration number'].sample(n=car_info_t2, replace=True).reset_index(drop=True)

random_cars = np.hstack((random_cars_t1, random_cars_t2))

car_info_df['car REF'] = random_cars



car_info_df_t1 = car_info_df.head(car_info_t1)
car_info_df_t2 = car_info_df.iloc[car_info_t1:car_info_number]
# print(car_info_df)

# RENTINGS
renting_number = 500000
renting_t1 = 200000
renting_t2 = 300000
unique_renting_numbers = set()
while len(unique_renting_numbers) < renting_number:
    unique_renting_numbers.add(generate_renting_number())

start_date_t1 = datetime(2022, 1, 1, 0, 0)
end_date_t1 = datetime(2022, 12, 12, 23, 59)

start_date_t2 = datetime(2023, 1, 1, 0, 0)
end_date_t2 = datetime(2023, 12, 12, 23, 59)
random_dates = []

for i in range(renting_number):
    if i < renting_t1:
        start_date = start_date_t1
        end_date = end_date_t1
    else:
        start_date = start_date_t2
        end_date = end_date_t2
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    random_dates.append(random_date)
random_dates.sort()
months = [date.month for date in random_dates]
end_dates = []
for day in random_dates:
    rent_duration = timedelta(hours=random.randint(0, 3), minutes=random.randint(0, 59))
    close_rent_date = day + rent_duration
    end_dates.append(close_rent_date)
renting_df = {
    'Renting number': list(unique_renting_numbers),
    'Start date': [date.strftime('%Y-%m-%d') for date in random_dates],
    'Start time': [date.strftime('%H:%M') for date in random_dates],
    'End date': [date.strftime('%Y-%m-%d') for date in end_dates],
    'End time': [date.strftime('%H:%M') for date in end_dates],
    'Month': months,
    'Start area': [random.choice('ABCDEFGHIJKLMN') for _ in range(renting_number)],
    'End area': [random.choice('ABCDEFGHIJKLMN') for _ in range(renting_number)],
    'Route lenght': [random.randint(0, 25000)/1000 for _ in range(renting_number)]
}
renting_df = pd.DataFrame(renting_df)
random_cars_to_rent_t1 = cars_df_t1['Registration number'].sample(n=renting_t1, replace=True).reset_index(drop=True)
random_cars_to_rent_t2 = cars_dataframe['Registration number'].sample(n=renting_t2, replace=True).reset_index(drop=True)
random_cars_to_rent = np.hstack((random_cars_to_rent_t1, random_cars_to_rent_t2))

random_client_to_rent_t1 = clients_df_t1['PESEL'].sample(n=renting_t1, replace=True).reset_index(drop=True)
random_client_to_rent_t2 = clients_dataframe['PESEL'].sample(n=renting_t2, replace=True).reset_index(drop=True)
random_client_to_rent = np.hstack((random_client_to_rent_t1, random_client_to_rent_t2))

renting_df['car REF'] = random_cars_to_rent
renting_df['client REF'] = random_client_to_rent
#print(renting_df['Start date'] + ' ' + renting_df['Start time'] + renting_df['End date'] + renting_df['End time'])

renting_df_t1 = renting_df.head(renting_t1)
renting_df_t2 = renting_df.iloc[renting_t1:renting_number]

# SURVEY
survey_number = 50000
random_rent = renting_df.sample(n=survey_number, replace=False).reset_index(drop=True)

survey_df = {
    'A. Date': random_rent['Start date'],
    'B. ID of rent': random_rent['Renting number'],
    'C. the biggest tackle': [generate_tackle_with_C() for _ in range(survey_number)],
    'D. we_vs_other_company': [random.randint(0, 1) for _ in range(survey_number)],
    'E. easiness_of_app': [random.randint(0, 1) for _ in range(survey_number)],
    'F. problems_during_rent': [random.randint(0, 1) for _ in range(survey_number)],
    'G. source': [generate_source_of_finding_out_G() for _ in range(survey_number)],
    'H. if recommendation': [random.randint(0, 1) for _ in range(survey_number)],
    'I. use services again': [random.randint(0, 1) for _ in range(survey_number)],
    'J. rate of satisfaction': [random.randint(0, 10) for _ in range(survey_number)]
}

survey_df = pd.DataFrame(survey_df)

# TO EXCEL
clients_df_t1.to_csv('clients_t1.csv', index=False)
clients_df_t2.to_csv('clients_t2.csv', index = False)

cars_df_t1.to_csv('cars_t1.csv', index=False)
cars_df_t2.to_csv('cars_t2.csv', index=False)

car_info_df_t1.to_csv('carInfo_t1.csv', index=False)
car_info_df_t2.to_csv('carInfo_t2.csv', index=False)

renting_df_t1.to_csv('rentings_t1.csv', index=False)
renting_df_t2.to_csv('rentings_t2.csv', index=False)

survey_df.to_excel('survey_sample.xlsx', index=False)

print("Gotowe")
