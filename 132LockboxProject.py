import Email
import GUI
import Randomizer
import Read
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.output(17, False)

cards = [35915910110]

Id = Read.Read()

if (Id in cards):
    message = Randomizer.random(4)
    Email.Email(message)
    GUI.Gui(message)
    
else:
    print "Access Denied"
    GPIO.cleanup()
    quit()
