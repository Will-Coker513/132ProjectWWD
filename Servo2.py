import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12,50)

def unlock():
    servo.start(2)
    time.sleep(.5)
    servo.stop()

def lock():
    servo.start(8)
    time.sleep(.5)
    servo.stop()
