# Animal Detection Using Raspberry Pi


This project requires the following equipments:
1. Raspberry Pi 
2. PIR (Passive Infrared) Sensor  (to detect motion)
3. A PushBullet Account (for getting notifications in your phone)

**STEPS**

**1. Create And Setup A Server To Host Push Notification Service **

 For getting notifications after detecting motion, you need the help of a server to host the push notification service and for that we are using 'Pushbullet', which is free and easy to use.
   1. Create an account on Pushbullet website
   2. Go to settings and click on CREAE ACCESS TOKEN button and copy the key that appear for putting it in the code later
   3. Now, install the PushBullet App from play store and sign in with the same account which you used to create the key
 
**2. Install PushBullet Libararies on Raspberry Pi**

   To install the required library for using Pushbullet on Raspberry Pi, run the following commands
     
       sudo apt-get update
       sudo apt-get upgrade
       sudo pip intall pushbullet.py
      
**3. Write The Python Code**

    The code to detect the motion using PIR sensor is in the motion_detection.py file
 
 
