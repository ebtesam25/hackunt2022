from email import header
import requests
import json

print('1 for water, 2 for food, 3 for drinks, 4 for tobacco, 5 for vehicles, 6 for general merch, 7 for energy')
inputR = float(input('What are we testing: '))
if inputR == 7:
    energy = float(input('What is the energy amount: '))
    #Eunits = input('What is the unit of energy: ')
    data = {
        "emission_factor": "electricity-energy_source_grid_mix",
        "parameters": {
            "energy": energy, 
            "energy_unit": "kWh"
        }
    }
elif inputR == 1:
    money = float(input('What is the money spent on water, in USD: '))
    data = {
        "emission_factor": "water-supply_wastewater_treatment",
        "parameters": {
            "money": money
        }
    }
elif inputR == 2:
    money = float(input('What is the money spent on food, in USD: '))
    data = {
        "emission_factor": "consumer_goods-type_all_other_foods",
        "parameters": {
            "money": money
        }
    }
elif inputR == 3:
    money = float(input('What is the money spent on beverages, in USD: '))
    data = {
        "emission_factor": "consumer_goods-type_beverages",
        "parameters": {
            "money": money
        }
    }
elif inputR == 4:
    money = float(input('What is the money spent on tobacco, in USD: '))
    data = {
        "emission_factor": "consumer_goods-type_tobacco_products",
        "parameters": {
            "money": money
        }
    }
elif inputR == 6:
    money = float(input('What is the money spent on general merchandise, in USD: '))
    data = {
        "emission_factor": "general_retail-type_general_merchandise_stores",
        "parameters": {
            "money": money
        }
    }
elif inputR == 5:
    print('1 for small truck, 2 for medium to large truck, 3 for passenger car, 4 for motorhome, 5 for motorcycle, 6 for vans / suvs, 7 for Bus, 8 for subway transit')
    vehicle = float(input('What type of vehicle are we checking: '))
    if vehicle == 4:
        money = float(input('How much money is spent on gas for the motorhome: '))
        data = {
            "emission_factor": "passenger_vehicle-vehicle_type_motor_homes-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "money": money
            }
        }
    elif vehicle == 1:
        miles = float(input('How many miles are driven in the small truck: '))
        data = {
            "emission_factor": "commercial_vehicle-vehicle_type_truck_light-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "distance": miles
            }
        }
    elif vehicle == 2:
        miles = float(input('How many miles are driven in the truck: '))
        data = {
            "emission_factor": "commercial_vehicle-vehicle_type_truck_medium_or_heavy-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "distance": miles
            }
        }
    elif vehicle == 3:
        miles = float(input('How many miles are driven in the passenger car: '))
        data = {
            "emission_factor": "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "distance": miles
            }
        }
    elif vehicle == 5:
        miles = float(input('How many miles are driven in the motorcycle: '))
        data = {
            "emission_factor": "passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "distance": miles
            }
        }
    elif vehicle == 6:
        money = float(input('How much money is spent on gas for the van or suv: '))
        data = {
            "emission_factor": "passenger_vehicle-vehicle_type_pickup_trucks_vans_suvs-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
            "parameters": {
                "money": money
            }
        }
    elif vehicle == 7:
        distance = float(input('How far did the bus travel in miles: '))
        data = {
            "emission_factor": "passenger_vehicle-vehicle_type_bus-fuel_source_na-distance_na-engine_size_na",
            "parameters": {
                "distance_unit": "mi",
                "distance": distance
            }
        }
    elif vehicle == 8:
        distance = float(input('How far did the subway transit travel in miles: '))
        data = {
            "emission_factor": "passenger_train-route_type_urban-fuel_source_na",
            "parameters": {
                "distance_units": "mi",
                "distance": distance
            }
        }
headers = {'Authorization': 'Bearer 2K6HSBYVPMM49QQXMCSANTTC45GA'}
json.dumps(data)
response = requests.post('https://beta3.api.climatiq.io/estimate', headers=headers, json=data)

print(response.json())

