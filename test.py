import Email
import GUI
import Randomizer
import Read

cards = [35915910110]

Id = Read()

if (Id in cards):
    print random(4)
else:
    print "Access Denied"
