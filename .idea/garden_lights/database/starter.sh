echo "Starting InfluxDB"
influxd -config /etc/influxdb/influxdb.conf > /tmp/influx.log 2>&1 &
echo "Waiting for InfluxDB to be started..."
sleep 5
echo "Starting MQTT/InfluxDB Bridge"
python3 /root/bridge.py