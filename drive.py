import obd
from apscheduler.schedulers.blocking import BlockingScheduler as scheduler
import requests
import json

speedList = []

maxSpeed = 0 #variable for the maxspeed as the loop implements
averSpeed = 0 #average speed variable as the loop implements
speedCntr = 0 #index for the amount of speed values stored in the speedList list
hardAccel = 0
hardDecel = 0
connection = obd.OBD() # auto-connects to USB or RF port
def speedf():
    cmd = obd.commands.SPEED # select an OBD command (sensor)
    response = connection.query(cmd) # send the command, and parse the response
    print(response.value) # returns unit-bearing values thanks to Pint
    speedList.append(response)
    for speed in speedList:
        speedCntr + 1
        if(speed > maxSpeed):
            maxSpeed = speed
        averSpeed = ((float(speed) + float(averSpeed)) / speedCntr)
        if(next(speed) - speed) >= 7:
            hardAccel + 1
        elif(speed - next(speed)) >= 9:
            hardDecel + 1

sch = scheduler()
sch.add_job(speedf, 'interval', seconds=1)

url = "https://us-central1-aiot-fit-xlab.cloudfunctions.net/greenscore"

payload = json.dumps({
  "action": "adddrivescore",
  "maxspeed": maxSpeed,
  "userid": "4",
  "miles": 15,
  "hac": hardAccel,
  "hb": hardDecel,
  "avspeed": averSpeed,
  "parking": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

connection.close()