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
                Id, text = reader.read()
                print(Id)
                print(text)
                return Id

        except KeyboardInterrupt:
                gpio.cleanup()
                

