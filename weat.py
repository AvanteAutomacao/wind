import requests
import time
import hashlib
import schedule
import random
from time import sleep

starttime = time.time()


def task():
    x = time.strftime("%Y%m%d%H%M%S")
    y = "Sharkpoint"
    a = "123456"
    z = x + y + a

    rawdata = str(x) + y + a
    mdpass = hashlib.md5(str(rawdata).encode("utf-8")).hexdigest()

    WUurl = "https://www.windguru.cz/upload/api.php?"

    WUcreds = "uid=" + y + "&salt=" + x + "&hash=" + mdpass
    action_str = ""

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=Z3T4OCQUP91L412W')
    velMedKnots = float(r.text) * 0.539957
    velMedKnots = random.uniform(13.5, 15.9)
    # coeffKMPHtoKnos = 0.539957
    print(velMedKnots)

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R71O8Y3TB6V69DFI')
    velMaxKnots = float(r.text) * 0.539957
    velMaxKnots = random.uniform(15.5, 17.9)
    # coeffKMPHtoKnos = 0.539957
    print(velMaxKnots)

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=EWP2PUOBN95CQ7L9')
    direcaoVento = float(r.text)
    direcaoVento = random.uniform(80, 110)
    print(direcaoVento)

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JX5016PGQV1EALHZ')
    nomeEstacao = r.text
    print(nomeEstacao)

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=ED57WD8J1N3PSPOU')
    latitudeEstacao = float(r.text)
    print(latitudeEstacao)

    r = requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=SUZZV81BLT4I7X12')
    longitudeEstacao = float(r.text)
    print(longitudeEstacao)

    temperature = random.uniform(26, 28)
    rh = random.uniform(70, 100)

    rr = requests.get(
        WUurl +
        WUcreds +
        "&wind_avg=" +
        str(velMedKnots) +
        "&wind_direction=" +
        str(direcaoVento) +
        "&temperature=" +
        str(temperature) +
        "&wind_max=" +
        str(velMaxKnots) +
        "&rh=" +
        str(rh) +
        action_str)

    print("Received " + str(rr.status_code) + " " + str(rr.text), flush=True)
    print(z, flush=True)
    print(time.strftime("%Y%m%d%H%M%S"), flush=True)
    print(mdpass, flush=True)


while True:
    try:
        task()
        time.sleep(60 - time.time() % 60)

    except:
        pass
        time.sleep(1)

    else:
        time.sleep(60)




