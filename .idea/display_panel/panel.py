# importing libraries
import paho.mqtt.client as mqtt
import time
import random
import requests
import pyowm
from datetime import datetime
import getpass
import ssl
import tkinter as tk


server=input("Enter the IP address of the IoT server: ")
user=input("Enter the username: ")
passw=input("Enter the password: ")
# #Get the data of the city and region
res = requests.get('https://ipinfo.io/')
data = res.json()
city = data['city']
region = data['region']
area = city + "," + region
owm = pyowm.OWM('242da1d9358bb234f6c62fcfabefb0c6')

def connectCallback(client, userdata, flags, rc):
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

def Draw():
    global text1,text2,text3,text4
    frame2=tk.Frame(root,width=100,height=100,relief='solid',bd=2)
    frame=tk.Frame(root,width=300,height=200)
    frame.place(x=40,y=80)
    frame2.place(x=100,y=10)
    text1=tk.Label(frame,text='Temperature')
    text2=tk.Label(frame,text='Condition')
    text3=tk.Label(frame2,text='Title')
    text4=tk.Label(frame,text='Room Temperature')
    text1.pack()
    text2.pack()
    text3.pack()
    text4.pack()

def Refresher():
    global text1,text2,text4
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city = data['city']
    region = data['region']
    area = city + "," + region
    owm = pyowm.OWM('242da1d9358bb234f6c62fcfabefb0c6')
    test = owm.weather_manager().weather_at_place(area).weather.status
    celsius = owm.weather_manager().weather_at_place(area).weather.temperature('celsius')['temp']
    print(celsius, test)
    client.subscribe("room/temperature")
    client.on_message=msgCallback
    room = status["temperature_level"]
    print(room)
    text1.configure(text="Outside Temperature: "f"{celsius}""℃ ", font=("Arial",16))
    text2.configure(text="Weather Condition: "f"{test}", font=("Arial",16))
    text4.configure(text="Room Temperature: "f"{room}""℃ ", font=("Arial",16))
    text3.configure(text="IOLink'eT", font=("Calibri",40), fg="white", bg="black")
    root.after(10000, Refresher)

status={"temperature_level":0}
mqtt.Client.connected_flag=False
mqtt.Client.bad_connection_flag=False
client =mqtt.Client("Panel", userdata=status)
client.username_pw_set(user,passw)
#client.tls_set("/root/ca.crt",certfile="/root/client.crt", keyfile="/root/client.key")
client.tls_set(ca_certs="/root/ca.crt",cert_reqs=ssl.CERT_NONE, tls_version=2)
client.on_connect=connectCallback
print("Connecting to server ",server)

client.loop_start()
try:
    print("Try block")
    client.connect(server,8883)
    while not client.connected_flag:
        print("Waiting for connection")
        time.sleep(1)
except:
    print("Connection Failed")
    exit("Quitting")

root=tk.Tk()
root.geometry("450x200")
root.resizable(False, False)
root.configure(bg="black")
Draw()
Refresher()
root.mainloop()

client.loop_stop()
client.disconnect()
