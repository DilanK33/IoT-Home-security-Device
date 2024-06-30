import machine
import urequests
import utime as time
import json
import network
from dht import DHT11
import secrets as s
import ubinascii
from simple import MQTTClient  

############ SENSOR DATA ############
# DHT11 Sensor
DHT_data_pin = 16
PIR_data_pin = 28
sound_data_pin = 15

myPin = machine.Pin(DHT_data_pin, machine.Pin.OUT, machine.Pin.PULL_DOWN)
sensor = DHT11(myPin)

# PIR sensor
PIR_pin = machine.Pin(PIR_data_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Sound sensor
sound_pin = machine.Pin(sound_data_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

############ WIFI CONNECTION ############

# Wi-Fi Information
Wifi_ssid = s.secrets["SSID"]
Wifi_pass = s.secrets["PASSWORD"]

# IFTTT Information
event_name = s.secrets["event_name"]
IFTTT_key = s.secrets["IFTTT_key"]
IFTTT_URL = f"/trigger/{event_name}/with/key/{IFTTT_key}"
server = "maker.ifttt.com"

############ SEND DATA TO ADAFRUIT IO ############

# Adafruit IO details
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = s.secrets['aio_username']
AIO_KEY = s.secrets['aio_key']
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
AIO_FEED_TEMP = "Temperature"
AIO_FEED_HUMID = "Humidity"
AIO_FEED_PIR = "Motion Detection"
AIO_FEED_SOUND = "Sound Detection"

client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

def client_connect():
    client.connect()
    print("Connected to Adafruit IO")

# Function to send data
def send_data(feed, value):
    client.publish(f"{s.secrets['aio_username']}/feeds/{feed}", str(value))

def wifi_connection():
    try:
        wifi=network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(Wifi_ssid, Wifi_pass)

        while not wifi.isconnected():
            print('Waiting for connection  .  .  .')
            time.sleep(1)
        print("Connected! Network configuration:", wifi.ifconfig())
    except Exception as e:
        print("Issues with Connection to WiFi!")
        print(e)

############ IFTTT ############

def ifttt_req():
    try:
        # Measure sensor data
        sensor.measure()
        tempC = sensor.temperature()
        hum = sensor.humidity()
        dht_data = f"Temperature: {tempC} Humidity: {hum}"
        motion_sensor = f"Motion Detected: {PIR_pin.value()}"
        sound_sensor = f"Sound Detected: {sound_pin.value()}"
        
        if motion_sensor == 0:
            motion_sensor = "0"
        elif sound_sensor == 0:
            sound_sensor = "0"
        elif motion_sensor == 0 and sound_sensor == 0:
            sound_sensor = "0"
            motion_sensor = "0"
        
        # Prepare data as dictionary
        data = {
            "value1": dht_data,
            "value2": motion_sensor,
            "value3": sound_sensor,
        }

        # Convert data to JSON string
        json_data = json.dumps(data)
        print(json_data)

        headers = {"Content-Type": "application/json"}
        url = f"https://{server}{IFTTT_URL}"
        print("Sending request to:", url)
    
        response = urequests.post(url, data=json_data, headers=headers)
        print("Response:", response.text)
        response.close()
    except Exception as e:
        print("Request failed:", e)
    
############ MAIN ############

if __name__ == "__main__":
    wifi_connection()
    client_connect()
    
    while True:
        # Example loop to send data
        try:
                # Sensor values
                sensor.measure()
                temperature = sensor.temperature()
                humidity = sensor.humidity()
                pir_value = PIR_pin.value()
                sound_value = sound_pin.value()
                
                # Send data to feeds
                send_data(AIO_FEED_TEMP, temperature)
                send_data(AIO_FEED_HUMID, humidity)
                send_data(AIO_FEED_PIR, pir_value)
                send_data(AIO_FEED_SOUND, sound_value)
                
                print(f"Sent data - Temp: {temperature}, Hum: {humidity}, PIR: {pir_value}, Sound: {sound_value}")
                
                time.sleep(20)

        except KeyboardInterrupt:
            print("Disconnected")
            client.disconnect()

        counter = 0
        counter += 1
        print(f"Uploading Values: {counter}")
        ifttt_req()
        time.sleep(1)
            
