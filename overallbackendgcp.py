import os
import pymongo
import json
import random
import hashlib
import time

import requests

from hashlib import sha256

def getemission(inputR, val2, val3):

    data = {}

    # print('1 for water, 2 for food, 3 for drinks, 4 for tobacco, 5 for vehicles, 6 for general merch, 7 for energy')
    # inputR = float(input('What are we testing: '))
    if inputR == 7:
        # energy = float(input('What is the energy amount: '))
        energy = val2
        #Eunits = input('What is the unit of energy: ')
        data = {
            "emission_factor": "electricity-energy_source_grid_mix",
            "parameters": {
                "energy": energy, 
                "energy_unit": "kWh"
            }
        }
    elif inputR == 1:
        # money = float(input('What is the money spent on water, in USD: '))
        money = val2
        data = {
            "emission_factor": "water-supply_wastewater_treatment",
            "parameters": {
                "money": money
            }
        }
    elif inputR == 2:
        # money = float(input('What is the money spent on food, in USD: '))
        money = val2
        data = {
            "emission_factor": "consumer_goods-type_all_other_foods",
            "parameters": {
                "money": money
            }
        }
    elif inputR == 3:
        # money = float(input('What is the money spent on beverages, in USD: '))
        money = val2
        data = {
            "emission_factor": "consumer_goods-type_beverages",
            "parameters": {
                "money": money
            }
        }
    elif inputR == 4:
        # money = float(input('What is the money spent on tobacco, in USD: '))
        money = val2
        data = {
            "emission_factor": "consumer_goods-type_tobacco_products",
            "parameters": {
                "money": money
            }
        }
    elif inputR == 6:
        # money = float(input('What is the money spent on general merchandise, in USD: '))
        money = val2
        data = {
            "emission_factor": "general_retail-type_general_merchandise_stores",
            "parameters": {
                "money": money
            }
        }
    elif inputR == 5:
        # print('1 for small truck, 2 for medium to large truck, 3 for passenger car, 4 for motorhome, 5 for motorcycle, 6 for vans / suvs, 7 for Bus, 8 for subway transit')
        # vehicle = float(input('What type of vehicle are we checking: '))
        vehicle = val2
        if vehicle == 4:
            money = val3
            # money = float(input('How much money is spent on gas for the motorhome: '))
            data = {
                "emission_factor": "passenger_vehicle-vehicle_type_motor_homes-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "money": money
                }
            }
        elif vehicle == 1:
            # miles = float(input('How many miles are driven in the small truck: '))
            miles = val3
            data = {
                "emission_factor": "commercial_vehicle-vehicle_type_truck_light-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "distance": miles
                }
            }
        elif vehicle == 2:
            # miles = float(input('How many miles are driven in the truck: '))
            miles = val3
            data = {
                "emission_factor": "commercial_vehicle-vehicle_type_truck_medium_or_heavy-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "distance": miles
                }
            }
        elif vehicle == 3:
            # miles = float(input('How many miles are driven in the passenger car: '))
            miles = val3
            data = {
                "emission_factor": "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "distance": miles
                }
            }
        elif vehicle == 5:
            # miles = float(input('How many miles are driven in the motorcycle: '))
            miles = val3
            data = {
                "emission_factor": "passenger_vehicle-vehicle_type_motorcycle-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "distance": miles
                }
            }
        elif vehicle == 6:
            # money = float(input('How much money is spent on gas for the van or suv: '))
            money = val3
            data = {
                "emission_factor": "passenger_vehicle-vehicle_type_pickup_trucks_vans_suvs-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
                "parameters": {
                    "money": money
                }
            }
        elif vehicle == 7:
            # distance = float(input('How far did the bus travel in miles: '))
            distance = val3
            data = {
                "emission_factor": "passenger_vehicle-vehicle_type_bus-fuel_source_na-distance_na-engine_size_na",
                "parameters": {
                    "distance_unit": "mi",
                    "distance": distance
                }
            }
        elif vehicle == 8:
            # distance = float(input('How far did the subway transit travel in miles: '))
            distance = val3
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

    # print(response.json())

    js = response.json()

    # print (js['co2e'])

    return js['co2e']



def sendsms(tonum, message):


    url = "https://us-central1-aiot-fit-xlab.cloudfunctions.net/sendsms"

    payload = json.dumps({
    "receiver": tonum,
    "message": message,
    "token": "redacted"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

def hashthis(st):


    hash_object = hashlib.md5(st.encode())
    h = str(hash_object.hexdigest())
    return h



def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()



    receiver_public_key = os.environ.get('ownpublic')

    mongostr = os.environ.get('MONGOSTR')
    client = pymongo.MongoClient(mongostr)
    db = client["greenscores"]


    retjson = {}

    action = request_json['action']






    if action == "getuseridfromphone":
        col = db.users

        for x in col.find():
            if x['phone'] == request_json['phone']:
                retjson['status'] = "found"
                retjson['name'] = x['name']
                retjson['id'] = x['id']
                retjson['balance'] = x['balance']

                return json.dumps(retjson)

        retjson['status'] = "unknown"
        retjson['name'] = "none"
        retjson['id'] = "-1"
        retjson['balance'] = 0

        return json.dumps(retjson)

    if action == "getstatus":
        col = db.status

        for x in col.find():
            if x['userid'] == request_json['userid']:
                retjson['status'] = x['status']
                retjson['miles'] = x['miles']
                retjson['avgspeed'] = x['avgspeed']
                retjson['location'] = x['location']

                return json.dumps(retjson)
        
        return json.dumps(retjson)


    if action == "getemissionsbyuser":
        col = db.emissions

        scores = []

        atype = ""

        for x in col.find():
            if x['userid'] == request_json['userid']:

                retjson['score'] = x['score']
                if x['val1'] == 1:
                    atype = "water"
                
                if x['val1'] == 2:
                    atype = "food"
                
                if x['val1'] == 3:
                    atype = "drinks"
                
                if x['val1'] == 4:
                    atype = "tobacco"
                
                if x['val1'] == 5:
                    atype = "vehicles"
                
                if x['val1'] == 6:
                    atype = "general merchandise"
                
                if x['val1'] == 7:
                    atype = "energy"
                


                retjson['activity'] = atype
                if x['val1'] == 5:
                    vtype = ""

                    retjson['vehicle type'] = vtype
                else:
                    retjson['val2'] = x['val2']
                retjson['val3'] = x['val3']
                retjson['co2'] = x['co2e']

                
                scores.append(retjson)

        
        retjson2 = {}

        retjson2['emissions'] = scores
        return json.dumps(retjson2)



    if action == "getuserdrivescore":
        col = db.drivescores

        scores = []

        for x in col.find():
            if x['userid'] == request_json['userid']:

                retjson['score'] = x['total']
                retjson['miles'] = x['miles']
                retjson['hardaccel'] = x['hac']
                retjson['hardbrake'] = x['hb']
                retjson['parking'] = x['parking']
                retjson['avspeed'] = x['avspeed']
                retjson['maxspeed'] = x['maxspeed']
                
                scores.append(retjson)
                
                

        
        retjson2 = {}

        retjson2['scores'] = scores
        return json.dumps(retjson2)


    if action == "getuserscore":
        col = db.greenscores

        scores = []

        for x in col.find():
            if x['id'] == request_json['userid']:

                retjson['score'] = x['score']
                # retjson['weeklymiles'] = x['weekly']

                scores.append(retjson)

        
        retjson2 = {}

        retjson2['scores'] = scores
        return json.dumps(retjson2)


    if action == "insurancehistory":
        userid = request_json['userid']

        col = db.paymenthistory
        
        curr = 0
        allpay = []
        currtotal = 0
        for x in col.find():
            if x['type'] == "insurance":
                if x['status'] == "current":
                    currtotal += x['amount']
                    if x['userid'] == userid:
                        curr = x['amount']
                else:
                    if x['userid'] == userid:
                        allpay.append(x['amount'])
        retjson['paymenttotal'] = currtotal
        retjson['userpayment'] = curr
        retjson['paymenthistory'] = allpay

        return json.dumps(retjson)



    if action == "addemission":
        
        maxid = 1
        col = db.emissions
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        val1 = int(request_json['val1'])
        val2 = int(request_json['val2'])
        val3 = int(request_json['val3'])

        co2e = getemission(val1, val2, val3)

        rawscore = -1.0 * float(co2e)
        basescore = 52.0 + rawscore 



        payload = {}

        uid = id 
        payload["id"] = id
        # payload["uid"] = request_json['uid']
        # payload["name"] = request_json['name']
        payload["val1"] = request_json['val1']
        payload["co2e"] = co2e
        payload["userid"] = request_json['userid']
        payload["val2"] = request_json['val2']
        payload["val3"] = request_json['val3']

        payload["score"] = basescore
        

        
        result=col.insert_one(payload)


        col = db.greenscores
        payload = {}
        payload["id"] = id


        payload["co2e"] = co2e
        payload["userid"] = request_json['userid']


        payload["score"] = basescore
        result=col.insert_one(payload)


        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['co2'] = co2e
        retjson['score'] = basescore
        

        return json.dumps(retjson)








    if action == "addgroup":
        
        maxid = 1
        col = db.groups
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)


        number = random.randint(1000,9999)

        invitecode = request_json['name'] + str(number)

        payload = {}

        uid = id 
        payload["id"] = id
        # payload["uid"] = request_json['uid']
        # payload["name"] = request_json['name']
        payload["name"] = request_json['name']
        payload["invitecode"] = invitecode
        payload["creator"] = request_json['userid']
        payload["pool"] = request_json['pool']
        payload["totalpool"] = request_json['pool']

        members = []
        members.append(request_json['userid'])
        payload["members"] = members
        

        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['groupid'] = id
        retjson['invitecode'] = invitecode
        

        return json.dumps(retjson)





    if action == "getallusers":
        col = db.users

        data = []

        for x in col.find():
            ami = {}
            
            ami["id"] = x["id"]
            ami["name"] = x["name"]
            
            ami["details"] = x["details"]
            ami["phone"] = x["phone"]
            ami["imageurl"] = x["imageurl"]
            ami['balance'] = x['balance']

            
            data.append(ami)

        retjson['users'] = data

        return json.dumps(retjson)








    if action == "getuserdata":
        col = db.users
        for x in col.find():
            if int(x['id']) == int(request_json['userid']):
                name = x['name']




                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['name'] = name  
                retjson['email'] = x['email']
                retjson['phone'] = x['phone']
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)


    if action == "updateuserdata":
        col = db.users
        for x in col.find():
            if int(x['id']) == int(request_json['id']):
                if 'name' in request_json:
                    col.update_one({"id": x['id']}, {"$set":{"name":request_json['name']}})
                    


                retjson = {}

                # retjson['dish'] = userid
                retjson['responsestatus'] = "success"

                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['id'] = "-1"

        return json.dumps(retjson)




    if action == "notifywinner":
        bidid = request_json['winnerid']

        col = db.users
        for x in col.find():
            if x['id'] == bidid:
                tonum = x['uphone']
                sendsms(tonum, "winner of this week")


                
                retjson = {}

                
                retjson['status'] = "success"
                
                

                return json.dumps(retjson)

        retjson['status'] = "fail -bid id not found"
        
        

        return json.dumps(retjson)





    if action == "adddrivescore" :
        maxid = 1
        col = db.drivescores
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        default = 100

        slimit = 70

        miles = request_json['miles']

        if request_json['avspeed'] > slimit:
            default -= 3*miles
        
        if request_json['maxspeed'] > slimit:
            default -= 10
        
        default -= request_json['hac']
        default -= request_json['hb']
        default -= request_json['parking']


        payload = {}

        uid = id 
        payload["id"] = id
        
        payload["miles"] = request_json['miles']
        payload["maxspeed"] = request_json['maxspeed']
        payload["total"] = default
        payload["parking"] = request_json['parking']
        payload["hac"] = request_json['hac']
        payload["hb"] = request_json['hb']
        payload["avspeed"] = request_json['avspeed']
        payload["userid"] = request_json['userid']


        
        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['drivescoreid'] = id

        return json.dumps(retjson)



    if action == "joingroup" :
        found = 0
        col = db.groups
        for x in col.find():
            if x["invitecode"] == request_json['invitecode'] and x['pool'] <= request_json['pool']:
                found = 1
                break

        if found == 0:
            retjson['status'] = "not found or pool amount mismatch"
            

            return json.dumps(retjson)

        col.update_one({'invitecode': request_json['invitecode']}, {'$push': {'members': request_json['userid']}})

        col.update_one({'invitecode': request_json['invitecode']}, {'$inc': {'totalpool': request_json['pool']}})


        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully joined"

        return json.dumps(retjson)






    if action == "register" :
        maxid = 1
        col = db.users
        for x in col.find():
            id = x["id"]
            maxid +=1
        id = str(maxid+1)

        payload = {}

        uid = id 
        payload["id"] = id
        # payload["uid"] = request_json['uid']
        # payload["name"] = request_json['name']
        payload["name"] = request_json['name']
        payload["email"] = request_json['email']
        payload["phone"] = request_json['phone']

        # payload['address'] = request_json['address']

        payload["password"] = request_json['password']


        
        result=col.insert_one(payload)

        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "successfully added"
        retjson['userid'] = id

        return json.dumps(retjson)


    if action == "login":
        col = db.users
        for x in col.find():
            if x['email'] == request_json['email'] and x['password'] == request_json['password']:
                userid = x['id']
                name = x['name']
                retjson = {}

                # retjson['dish'] = userid
                retjson['status'] = "success"
                retjson['name'] = name
                retjson['userid'] = userid
                

                return json.dumps(retjson)
        retjson = {}

        # retjson['dish'] = userid
        retjson['status'] = "fail"
        retjson['userid'] = "-1"

        return json.dumps(retjson)




    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
