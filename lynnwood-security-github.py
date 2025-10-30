#security-lynnwood-oct 27-2025  no write unless switched on
#        Channel ID: 2392138        Author: ShoreNice
# Thanks always to Hippy for rock solid wifi code
import machine
import urequests
from machine import Pin,Timer
import network, time
import utime
import math

d1 = Pin(14, Pin.IN, Pin.PULL_UP) # switch
#reads the state of a button connected to GPIO pin 14.
#With the pull-up resistor enabled, the pin will read 1
#(high) when the button is not pressed. If the button is
#connected to ground (GND) and pressed, the pin will read 0 (low).

d2 = Pin(20, Pin.IN) # front_stair_pir_46
d3 = Pin(21, Pin.IN) # laundry_pir_55
d5 = Pin(28, Pin.IN, Pin.PULL_UP) # laundry_2_doors_48 &_53
d7 = Pin(27, Pin.IN) # kitchen_pir_58
d8 = Pin(22, Pin.IN, Pin.PULL_UP) # small_garage_door_50
saved_D1 = 0
saved_D2 = 0
saved_D3 = 0
saved_D5 = 0
saved_D7 = 0
saved_D8 = 0
#######
led = Pin("LED", Pin.OUT)  #pico w led flasher
tim = Timer()
HTTP_HEADERS = {'Content-Type': 'application/json'}
THINGSPEAK_WRITE_API_KEY = 'H845secret897J4'  
 
ssid = 'PEsecretG2'
password = 'WPKsecret3?'

# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
for _ in range(10):
        print('connecting to network...')
        sta_if.connect(ssid, password)
        time.sleep(1)
        if sta_if.isconnected():
            print('Connected.')
            break
        time.sleep(11)
 
print('network config:', sta_if.ifconfig())
def tick(timer):
    global led
    led.toggle()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

while True:
   
   time.sleep(1)
    ################################
 
   D1 = d1.value()
   D2 = d2.value()
   D3 = d3.value()
   D5 = d5.value()
   D7 = d7.value()
   D8 = d8.value()
   
  # typical: If this D1 value does not match our saved_D1, then
  # a transition has occurred and we should save the D1
  # This works both for open-to-close transitions and close-to-open transitions
 
   if ( D1 != saved_D1):
        saved_D1 = D1
        print("switch_status:       ", D1)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    time.sleep(1)
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            machine.reset()
   
   
   D2 = d2.value()
  # typical: If this D2 value does not match our saved_D2, then
  # a transition has occurred and we should save the D2
  # This works both for open-to-close transitions and close-to-open transitions
 
   if ( D2 != saved_D2)&(D1==1):
        saved_D2 = D2
        print("front_stair_pir_status:       ", D2)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    time.sleep(1)
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            
            machine.reset()
   
   D3 = d3.value()

   if ( saved_D3 != D3)&(D1==1):
        saved_D3 = D3
        print("laundry_pir_status:             ", D3)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            machine.reset()
   
   D5 = d5.value()

   if ( saved_D5 != D5)&(D1==1):
        saved_D5 = D5
        print("laundry_2_doors_status:        ", D5)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            machine.reset()
   
   
   D7 = d7.value()

   if ( saved_D7 != D7)&(D1==1):
        saved_D7 = D7
        print("kitchen_pir_status:          ", D7)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            machine.reset()
   
   D8 = d8.value()

   if ( saved_D8 != D8)&(D1==1):
        saved_D8 = D8
        print("small_garage_door_status:       ", D8)
        readings = {'field1':D1,'field2':D2,'field3':D3,'field5':D5,'field7':D7,'field8':D8}
        for retries in range(60):     # 60 second reboot timeout
            if sta_if.isconnected():
                print("Connected, sending")
                try:
                    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = readings, headers = HTTP_HEADERS )  
                    request.close()
                    print("Write Data to ThingSpeak ",readings)
                    print(" Successful  ")
                    time.sleep(15)
                    break
                except:
                    print("Send failed")
                    
            else:
                    print(" waiting for wifi to come back.....")
                    
        else:
            print("Rebooting")
            machine.reset()
   

 
print("Sent, waiting awhile")
time.sleep(1)


