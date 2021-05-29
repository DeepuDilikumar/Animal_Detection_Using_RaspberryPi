#Using Raspberry Pi and PIR (Passive Infrared) Sensor to detect motion (thereby animals) in farm

from pushbullet import Pushbullet   #importing Push Bullet library for giving notifications when motion detected
import RPi.GPIO as GPIO        #importing GPIO (General Purpose Input Output) module
from time import sleep         

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
pb = Pushbullet("ACCESS TOKEN YOU GOT FROM PUSHBULLET")  #Enter the access token that you copied while creating account on PushBullet
print(pb.devices)                                         #Printing all the devices that are using this account

while True:
  i = GPIO.input(11)                       #getting input from pin 11 which is from PIR sensor
  if i==0:                                #i==0, means no motion is detected
    sleep(1)
  elif i==1:                              #i==1, means motion detected
    dev = pb.get_device("Redmi 9")        #Your phone should be the argument
    push = dev.push_note("An animal detected in your farm")      #Message that you want to give is given as argument
    sleep(1)

