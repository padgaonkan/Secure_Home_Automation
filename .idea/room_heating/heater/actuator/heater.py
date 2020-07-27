import paho.mqtt.client as mqtt
import time
import ssl

cl_name="heater"
server=input("Enter the IP address of the IoT server: ")
user=input("Enter the username: ")
passw=input("Enter the password: ")

def connectCallback(c, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("Connected to the server")
        print(str(rc))
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

def msgCallback(c, userdata, message):
    print("Message recieved: %s, in topic %s"%(message.payload, message.topic))
    userdata["temperature_level"]=float(message.payload)

status={"heater_on":False, "temperature_level":0 }

client =mqtt.Client(cl_name, userdata=status)
mqtt.Client.connected_flag=False
mqtt.Client.bad_connection_flag=False
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

threshold=18

while True:

    time.sleep(10)
    client.subscribe("room/temperature")
    client.on_message=msgCallback
    if status["temperature_level"] == 0:
        print("Loading...")
    elif status["temperature_level"] < threshold:
        status["heater_on"]=True
        client.publish("heater/status",1)
        client.publish("heater/temperature_level",status["temperature_level"])
        print("Current temperature is %s and the heater is ON"%status["temperature_level"])
    else:
        status["heater_on"]=False
        client.publish("heater/status",0)
        client.publish("heater/temperature_level",status["temperature_level"])
        print("Current temperature is %s and the heater is OFF"%status["temperature_level"])


client.loop_stop()
client.disconnect