import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)	#Use physical pin numbering

GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.OUT)        #for any output tool (led,buzzer)

while True:
    i=GPIO.input(7)
    if i==0:                 #When output from motion sensor is LOW
        print("No motion",i)
        GPIO.output(13, GPIO.LOW)  #Turn OFF output tool
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Motion detected !!!",i)
        GPIO.output(13, GPIO.HIGH)  #Turn ON output tool
        time.sleep(0.1)
GPIO.cleanup()
