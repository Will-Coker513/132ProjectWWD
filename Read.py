#!/usr/bin/env python

def Read():
        GPIO.setwarnings(False)
        import RPi.GPIO as gpio
        import sys
        from mfrc522 import SimpleMFRC522

        gpio.setmode(gpio.BCM)

        reader = SimpleMFRC522()

        try: 
                print("place tag")
                id, text = reader.read()
                print(id)
                print(text)

        except KeyboardInterrupt:
                gpio.cleanup()
                
Read()
