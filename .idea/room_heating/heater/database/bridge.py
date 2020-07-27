import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import ssl

INFLUXDB_ADDRESS = '127.0.0.1'
INFLUXDB_USER = 'noel'
INFLUXDB_PASSWORD = 'Skodalaura-6903'
INFLUXDB_DATABASE = 'heater_db'

MQTT_ADDRESS = input("Enter the IP address of the MQTT server: ")
MQTT_USER=input("Enter the username: ")
MQTT_PASSWORD=input("Enter the password: ")
MQTT_TOPIC = 'heater/#'
MQTT_CLIENT_ID = 'heater_db'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to the server")
        print(str(rc))
        client.subscribe(MQTT_TOPIC)
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, msg):
    sensor_data = process_message(msg.topic, msg.payload.decode('utf-8'))

def process_message(topic, payload):
    if topic.startswith("heater/"):

        sensor=topic.split("/")[1]
        data=float(payload)
        json_body = [
            {
                'measurement': sensor,
                'fields': {
                    'value': data
                }
            }
        ]
        influxdb_client.write_points(json_body)
        print("Recorded value %.1f for %s"%(data,sensor))
    return None


def init_db():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)


def main():
    init_db()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.tls_set(ca_certs="/root/ca.crt",cert_reqs=ssl.CERT_NONE, tls_version=2)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS,8883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()