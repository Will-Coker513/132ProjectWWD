import Email
import GUI
import Randomizer
import Read

cards = [35915910110]

Id = Read.Read()

if (Id in cards):
    message = Randomizer.random(4)
    Email.Email(message)
    GUI.Gui(message)
    # if(GUI.unlocked = True):
        
else:
    print "Access Denied"
