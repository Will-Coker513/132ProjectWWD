import RPi.GPIO as GPIO
import time

servo = GPIO.PWM(7,50)

while True:
    servo.start(2)
    time.sleep(1)
    servo.ChangeDutyCycle(4)
    time.sleep(1)
    servo.ChangeDutyCycle(6)
    time.sleep(1)
    servo.ChangeDutyCycle(8)
    time.sleep(1)
    servo.ChangeDutyCycle(10)
    time.sleep(1)
    servo.ChangeDutyCycle(12)
    time.sleep(1)
