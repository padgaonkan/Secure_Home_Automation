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

def increase():
    value = float(lbl_value["text"])
    while value<30.0:
        new_val=value+0.5
        lbl_value["text"] = f"{new_val}"
        print("Sending temperature value %.1f"%new_val)
        client.publish("room/temperature","%.1f"%new_val)
        break

def decrease():
    value = float(lbl_value["text"])
    while value>10.0:
        new_val=value-0.5
        lbl_value["text"] = f"{new_val}"
        print("Sending temperature value %.1f"%new_val)
        client.publish("room/temperature","%.1f"%new_val)
        break

def connectCallback(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("Connected to the server")
        print(str(rc))
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

mqtt.Client.connected_flag=False
mqtt.Client.bad_connection_flag=False
client =mqtt.Client("Temperature")
client.username_pw_set(user,passw)
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

while True:
    new_val = 21.0
    print("Sending temperature value %.1f"%new_val)
    client.publish("room/temperature","%.1f"%new_val)
    window = tk.Tk()
    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    btn_decrease = tk.Button(master=window, text="-", command=decrease)
    btn_decrease.grid(row=0, column=0, sticky="nsew")

    lbl_value = tk.Label(master=window, text="21.0", command=print(21.0))
    lbl_value.grid(row=0, column=1)

    btn_increase = tk.Button(master=window, text="+", command=increase)
    btn_increase.grid(row=0, column=2, sticky="nsew")

    window.mainloop()
client.loop_stop()
client.disconnect()