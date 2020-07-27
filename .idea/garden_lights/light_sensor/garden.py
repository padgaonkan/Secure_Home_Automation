import paho.mqtt.client as mqtt
from datetime import datetime
import requests
from astral import LocationInfo
from astral.sun import sun
import time
import ssl

cl_name="garden_lights" #name of the client
server=input("Enter the IP address of the IoT server: ")
user=input("Enter the username: ")
passw=input("Enter the password: ")

res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
region = data['region']
zone = data['timezone']
location = LocationInfo(city,region)

# display message to user when server is connected
def connectCallback(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("Connected to the server")
        print(str(rc))
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

# connecting to the server and starting the loop function
mqtt.Client.connected_flag=False
mqtt.Client.bad_connection_flag=False
client =mqtt.Client(cl_name)
client.username_pw_set(user,passw)
client.tls_set(ca_certs="/root/ca.crt",cert_reqs=ssl.CERT_NONE, tls_version=2)
client.on_connect=connectCallback
print("Connecting to server ",server)

client.loop_start()

try:
    client.connect(server,8883)
    while not client.connected_flag:
        print("Waiting for connection")
        time.sleep(1)
except:
    print("Connection Failed")
    exit("Quitting")

while True:
    s = sun(location.observer, date=datetime.now().date(), tzinfo=zone)
    sunrise = s["sunrise"].strftime("%Y-%m-%d, %H:%M:%S")
    sunset = s["sunset"].strftime("%Y-%m-%d, %H:%M:%S")
    current_datetime=datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    time.sleep(10)
    if current_datetime <= sunrise or current_datetime >=sunset:
        print("Garden Lights are ON")
        client.publish("garden/status",1)
    else:
        print("Garden Lights are OFF")
        client.publish("garden/status",0)
client.loop_stop()
client.disconnect()

