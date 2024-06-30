# **Home Security Device: For Fires & Intruders**
Author: Dilan Karkawatli (dk222tu)

---
### **Project Overview**
This tutorial will guide you through finding the right equipment, building, coding and achieving wifi connection with a home security system, all by yourself. The device itself will allow you to monitor your temperature & humidity for fires, motion where motion is unexpected and sound incase of the fire alarm or any other unexpected sounds. 

### **Time Estimation**
You should always include time for finding solutions to errors. Every system is different and can have its own unique problems. But I leave that estimation for you. 

The raw time estimate for building (with all the tools and equipment at your disposal) is about 4-8 hours. 

## **Objective**
With this device, I want to achieve responsability from afar. By keeping track of sounds, temperature, humidity and motion, I can be sure of things I couldn't be sure of before. A reasonable extension for this project is to start recording whenever a sound is heard. That way you can keep track of how many has knocked, what kind of sounds are heard and of course in worst case scenarios, gather intel for investigations or for yourself. A home made security system!

With the data I can also keep track of the quitness of the apartment, perhaps in the household, movements but most usefully, the temperature and humidity when I'm gone. I expect it to be a second pair of ears for when I'm not home and my phone will be able to notify me of when things start to move and when sounds are heard. This I feel, is super useful and desired.

### **Material**
|Image| Electronic Equipment    |Usage| Price
|-| ----------------------- |-|-----------
|![image](https://hackmd.io/_uploads/r1hTTCCIR.png)| [Raspberry Pi Pico WH](https://www.electrokit.com/raspberry-pi-pico-wh?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc0HbZgsfjdPbt29OsL31Ca_33VCZcLr-qJRmKLGbZ5ehC1NOBJIXTxoCb4EQAvD_BwE)    |A microcontroller that can manage IoT projects well with its built in wifi. It has 30 GPIO pins in total with ground pins, voltage pins (3.3V), a VBUS etc. Click [here](https://www.farnell.com/datasheets/3759470.pdf) for more information.| 11$/110 SEK 
|![image](https://hackmd.io/_uploads/ByY1R0A8R.png)| [Breadboard](https://www.kjell.com/se/produkter/el-verktyg/elektronik/elektroniklabb/luxorparts-kopplingsdack-400-anslutningar-2-pack-p36283?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc47mbDig_fVTlgCPkR4q1S5fAYuNspzyCBRJskbv-sZmHDqlpgL_yBoCT9UQAvD_BwE) |A good way to practice and test electrical solutions temporarily without soldering on and off components. It has positive and negative lanes on each edge which needs to be understood before used. It also has a row and column system. Click [here](https://uk.rs-online.com/web/content/discovery/ideas-and-advice/breadboard-guide) for more.| 10$/100 SEK
|![image](https://hackmd.io/_uploads/rJuXR00L0.png)| [Lab Wires (Male-Male)](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane)   |Connect easily to two points in a breadboard for example.| 3$/30 SEK 
|![image](https://hackmd.io/_uploads/rky8CC0IA.png)| [Lab Wires (Female-Male)](https://www.electrokit.com/labbsladd-20-pin-15cm-hona/hane)|The female port is used only for the PIR sensor as it has components sticking out of both ends so it can't be connected to a breadboard. So its three pins are connected to female wires then male wires connect to the breadboard.| 3$/30 SEK
|![image](https://hackmd.io/_uploads/B1snRRA8R.png)| [Micro-USB to USB-C or USB)](https://www.teknikdelar.se/produkt/deltaco-micro-usb-kabel-2-m-svart?dv_adwords_campaign=21114826225&dv_adwords_network=x&dv_adwords_target&gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhcxnCIz5WirwI_EGVxGlBKPtdZuVJz6K2Fs1O4ljpPxb2B9mSDorIEhoCvyYQAvD_BwE) |A simple micro-usb to usb or usb-c wire. Make sure to check if it can be used efficiently for data transfer. If there are any errors with the data transfer, check your wire.| 4$/40 SEK
|**Total**||| **31$/210 SEK**

|Image| Sensors |Usage| Price    |
|-| -------- |-| -------- |
|![image](https://hackmd.io/_uploads/HJcfpARIA.png)| [PIR motionsensor HC-SR501](https://www.electrokit.com/pir-rorelsedetektor-hc-sr501?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc5zcle1eDoCvlVrlgXlb5Vc4veF4guax2gvllXW4OC4UusBdxewH7xoCoqMQAvD_BwE)     |A motion detection sensor that detects light. Two properties of this sensor can be tuned with a phillips screwdriver. One is its light sensitivity and second is its hold time (time it takes to update to the next value)| 4$/50 SEK
|![image](https://hackmd.io/_uploads/BJdBTARLC.png)| [Sound Sensor (Digital & Analog)](https://www.electrokit.com/ljudsensor-analogdigital?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc4gkOS6NGZSMkXpHFesaP28sxo-UNPjQWvNMqGXIQ_7X1HcIPUk9ehoCDLoQAvD_BwE)|A sensitive sensor that uses a small microphone to measure sound. Its sensitivity can be tuned with a really small flathead screwdriver. It is almost a given that you need to tune it, so be prepared. (I had to use my girlfriends hair pin!)| 3$/30 SEK
|![image](https://hackmd.io/_uploads/r1_vp00UR.png)| [DHT11 (Four Pins)](https://www.electrokit.com/temp/fuktsensor-dht11?gad_source=1&gclid=CjwKCAjwhIS0BhBqEiwADAUhc1mPL-oYvKCaoiRrJSqSP0ppjeONaF6YzEIx5JwLlUWddF2RxagV0hoCOWoQAvD_BwE)     |A small temperature and humidity sensor.| 4$/40 SEK    |
|**Total**|      || **11$/110 SEK**    |

#### **I bought mine [here](https://www.electrokit.com/lnu-starter).**


## **Computer setup**
The pico WH is easiest programmed with **thonny**. I used VS Code for the majority of the project and I had a lot of issues. When I tried out thonny it solved almost all issues and made the remaining issues easier to solve. It is easy to setup, click the [link](https://thonny.org/) and download it to your system. 

When you have it, leave it for a moment and [download](https://micropython.org/download/RPI_PICO_W/) micropython to your device. Hold the BOOTSEL button on the pico when connecting it to your computer. That will open the PICO WH's files and you can just drag and drop the UF2 file. It will close after it's been copied and you can start using it! Here's a [video](https://www.youtube.com/watch?v=4efe8wPG6xE) on it. This is known as flashing the pico WH.

The first step to starting to program with the robot is to have all the modules ready. Download pymakr if you're on vscode, otherwise, start by copying this code on to the IDE and run it using the run button. 

```
from machine import Pin
import utime as time

# Define the GPIO pin number connected to the LED
led = Pin(25, Pin.OUT)

while True:
     led.value(1)
     time.sleep(1)
```

Next, you'll setup ifttt. Create an account and press create a new applet. Press add and find webhooks. Pick "choose web request" and name it. Keep it simple as you'll use it in your code. In the second step, click add again and search for notifications. When in choose “Send a notification from the IFTTT app”. Type your personalised message and press create action. To finalize the part, you'll just have to add the google sheets section. Click on add another action, search "google sheets" and personalise your row. I have multiple rows of data for this project so type something like this:
```
{{OccurredAt}}, {{Value1}}, {{Value2}}, {{Value3}}
```
OccurredAt adds the timestamp of the data and the rest are just values seperated by a comma. If you want to add in seperate cells type "|||" between values where the commas are, and remove the space and comma.

Now log into your google sheets account, setup your code and test the values you're getting. 

Note: Make sure to follow the correct [format](https://maker.ifttt.com/use/hBK3z3QTXHmcZuYqrd-3eraeSaxqwph2xa2lV6mPXw0)
 shows here to facilitate that the data is being sent to sheets. It has to be a dictionary with the key being called "value1" etc. 
 
```
{ "value1" : "", "value2" : "", "value3" : "" }
```

Here's [my code](https://github.com/DilanK33/IoT-Home-security-Device/blob/main/wifi_connection.py) for you to follow along. 

## **Putting everything together**

|![image](https://hackmd.io/_uploads/rJ2yTJkwA.png)| Pico WH Pins | DHT11 Pins (Four) |Use|
|-| -------- | -------- | -------- |
||      3V3(OUT)| VCC     | Power     |
||      GP16| OUT     | Data     |
|Not Used|     -| NC     | -     |
||      GND| GND     | Ground     |

|![image](https://hackmd.io/_uploads/SkfxCykw0.png)| Pico WH Pins | PIR Pins |Use|
|-| -------- | -------- | -------- |
||      VBUS (+3.3V)|3.3V to 5V     |   Power   |
||      GP28| OUT     | Data     |
||     GND| GND     | Ground     |


|![image](https://hackmd.io/_uploads/r1saCJkwA.png)| Pico WH Pins | Sound Sensor Pins |Use|
|-| -------- | -------- | -------- |
|Not Used|      -| Analog Out (AO)    |   -   |
||      GND| GND     | Ground     |
||     3V3(OUT)| VCC     | Power     |
||     GP15| Digital Out (DO)   | Data     |

*Be sure to use the positive and negative lanes of the breadboard. Because there are so many sensors you need to be efficient with the space on the breadboard. So connect ground from the Pico to one lane and 3V3(OUT) to another. That way you only need to connect to the respective lane for GND or 3V3(OUT).*

**Circuit Diagram**
![image](https://hackmd.io/_uploads/SJMRMeJP0.png)


## **Platform**
I chose IFTTT because of its wide array of possible implementations and for its access to connect to the phone, which I thought would be the hardest part. It is really easy to use, especially together with a google sheets document for data storage. It is a simple solution, which doesn't have to be bad, but also a good one as it give me the possability to extract the data as a .csv file which can then be used in all kinds of things like machine learning or data analytics. 

The platform is cloud-based. It is free for two applets, so two projects let's say, and it has a paid option for 20 projects for 3 bucks which is not bad. If I'd scale my home security idea I would want to use a database and slowly try to implement time costing stuff by myself so it runs smoother and in my control rather than using a large service like IFTTT. 


## **Code**
My code has imports highest up, definitions, then function definitions and lastly the main part of the code which handles the code.

**Imports**
```
import machine
import urequests
import utime as time
import json
import network
from dht import DHT11
import secrets as s # Secrets file on Pico
import ubinascii
from simple import MQTTClient # umqtt.simple
```

**Definitions (In order)**
* Pin definitions to gather data from sensors
* Wifi information (SSID, Passoword)
* IFTTT information (name, key, url)
* Adafruit definitions (username, feeds, etc)

**Function Definitions**
* client_connect(): Connect the defined (from definitions part) client 
* send_data(feed, value): Send data to client's information defined above.
* wifi_connection(): Connect to wifi using secrets file.
* ifttt_req(): Send data to sheet document using ifttt format.


**Main Code**
```

if __name__ == "__main__":
    wifi_connection()
    client_connect()
    
    while True:
        try:
            # Send data to adafruit
            ...
        except:
            ...

        counter = 0
        counter += 1
        print(f"Uploading Values: {counter}")
        # Upload value to sheets document
        ifttt_req()
        time.sleep(1)
```

By using the information needed such as keys and password for local wifi and ifttt wifi, I can connect the data values collected by my program with ifttt which then connects me with the google sheets document. This way I can send data through to the cloud to google drive. The wifi_connection() function uses a json function that reformats the dictionary I defined in that same function into a json friendly format which is needed for ifttt to work. 

In summary, I connect to the wifi, then, when connected, I am able to connect to adafruit so start sending data.

## **Transmitting the Data & Connectivity**
The data is being sent via my code to both IFTTT and adafruit. From IFTTT, a notification to the listed phone is sent and the data is written on the specified google sheets document in your specified format. The data is transmitted via internet using FTP (File Transfer Protocol). The data is sent to adafruit IO every 30 seconds and is updated on the google sheets every 10 seconds.

I am using WiFi as previously stated and using a webhook transport protocol, which in turn use the HTTP protocol as it is web based.

## **Presenting the data**
The dashboard is build by using two binary values from the motion sensor and the sound sensor, either it's on or off, so that is why I use a red or green circle to show if it was triggered or not. Then, I have a table that updates everytime there is a new reading from the temperature and humidity. Lastly, two gauges for both temperature and humidity aswell to simplify intuitive reading of the dashboard. 

![image](https://hackmd.io/_uploads/rJxFSJJDR.png)

The data is stored in a google sheets file and is auto saved. It is easy to scroll through, copy, delete or export and works really well in the IFTTT framework.

## **Final Results & Conclusion**
I liked how the project went. I really liked the building part and getting everything working. I think it is a good project and a useful one as it can be placed near your door and powered by a power outlet somewhere (a computer or a power bank has to act as a middle man). I still have to tweak the sensitivity of the sound sensor as it sometimes only prints ones and sometimes only zeroes and the threshold is really small and hard to work with. I think further steps are to build a non suspecting box, get a microphone for recording audio files and perhaps even a small camera that records the door and it all gets sent to my phone! Other than that, it was really fun that I got to do this and that I actually used almost every component I bought for the project. 

![image](https://hackmd.io/_uploads/B1jPMe1w0.png)

![image](https://hackmd.io/_uploads/Skp9ze1wC.png)


