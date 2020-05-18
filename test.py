######################################################################
# Name: Will Coker, Dylan Weaver, William Caverlee
# Date: 5/18/2020
# Description: Lockbox code using RFID, random, GUI, servo, and email
######################################################################

# title
# new user - write - submit
# title - unlock - read - random - email 
# keypad - Servo

from Tkinter import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
import smtplib
import time
from random import randint

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.output(17,False)
GPIO.output(12,False)

class Title(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        parent.attributes("-fullscreen", True) 
        self.setUpGui()

        
        
    def setUpGui(self):
        self.display = Label(self, text = "", anchor = E, bg = "white",\
                                height = 1, width = 15, font = ("TexGyreAdventor", 45))
            
        self.display.grid(row = 0, column = 0, columnspan = 4,\
                              sticky = N+E+W+S)

        self.pack(fill = BOTH, expand = 1)

        for row in range(5):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(2):
            Grid.rowconfigure(self, col, weight = 1)

        ###############Buttons################
        #Welcome!
        img = PhotoImage(file = "Keypad/images/Welcome.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : None 
        button.image = img
        button.grid(row = 33, column = 1, sticky = N+E+W+S)
        
        #New User
        img = PhotoImage(file = "Keypad/images/NewUser.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda :  StartSubmit())
        button.image = img
        button.grid(row = 4, column = 0, sticky = N+E+W+S)

        #Unlock
        img = PhotoImage(file = "Keypad/images/Unlock.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : Start())
        button.image = img
        button.grid(row = 4, column = 2, sticky = N+E+W+S)
        return 

def StartTitle():
    TitleScreen = Tk()

    TitleScreen.title("Keypad")

    t = Title(TitleScreen)

    TitleScreen.mainloop()

######################## END TITLE SETUP ##############################################################

######################## BEGIN SUBMIT/NEW USER SETUP #################################################

class SubmitButton(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        
        self.label = Label(master, text = "Enter email")
        self.label.pack(side = LEFT)
        self.entry = Entry(master)
        self.entry.pack(side = LEFT)
        self.button1 = Button(master, text = "Submit",command = self.Submit())
        self.button1.pack(side = LEFT)
        
        def setUpGui(self):
        self.display = Label(self, text = "", anchor = E, bg = "white",\
                                height = 1, width = 15, font = ("TexGyreAdventor", 45))
            
        self.display.grid(row = 0, column = 0, columnspan = 4,\
                              sticky = N+E+W+S)

        self.pack(fill = BOTH, expand = 1)

        for row in range(5):
            Grid.rowconfigure(self, row, weight = 1)
        for col in range(2):
            Grid.rowconfigure(self, col, weight = 1)

        self.display["text"] = "Place tag"
        textInput = self.entry.get()
        Write(textInput)
        self.display["text"] = "written"

    def Submit(self):
        Id, text = Read()
        self.display["text"] = "Place tag"
        cards.append(Id)
        s.withdraw()
        t.lift()

def StartSubmit():
    SubmitScreen = Tk()
    S = SubmitButton(SubmitScreen)
    SubmitScreen.mainloop()

######################### END SUBMIT SETUP ############################################################

######################### WRITE FUNCTION ##############################################################

def Write(placeholder):
    writer = SimpleMFRC522()

    try:
            text = str(placeholder)
            
            writer.write(text)
            

    except KeyboardInterrupt:
            GPIO.cleanup()

########################## END WRITE FUNCTION ##########################################################

########################## READ FUNCTION ###############################################################

def Read():
        reader = SimpleMFRC522()

        try:
                Id, text = reader.read()
                return Id, text

        except KeyboardInterrupt:
                GPIO.cleanup()
                        
########################## RANDOM FUNCTION #############################################################

def random(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)

########################## END RANDOM FUNCTION #########################################################

########################## EMAIL FUNCTION ##############################################################

def Email(message, text):

    smtpUser = "132raspberrypi@gmail.com"
    smtpPass = "Wc132Rpi8"

    toAdd = str(text)
    fromAdd = smtpUser

    subject = "Randomly Generated Code for Lock"
    header = "To: " + toAdd + "\n" + "From: " + fromAdd + "\n" + "Subject: " + subject
    body = str(message)

    # print header + "\n" + body

    s = smtplib.SMTP("smtp.gmail.com",587)

    s.ehlo()
    s.starttls()

    s.login(smtpUser, smtpPass)
    s.sendmail(fromAdd, toAdd, header + "\n\n" + body)

    s.quit()
    return 

########################## END EMAIL ###################################################################

########################## BEGIN KEYPAD GUI SETUP ######################################################

class Keypad(Title):
        def __init__(self, parent):
            Title.__init__(self, parent, bg = "white")
            parent.attributes("-fullscreen", True) 
            self.setUpGui()

            self.unlocked = False
            

        def setUpGui(self):
            self.display = Label(self, text = "", anchor = E, bg = "white",\
                                 height = 1, width = 15, font = ("TexGyreAdventor", 45))
            
            self.display.grid(row = 0, column = 0, columnspan = 4,\
                              sticky = N+E+W+S)

            self.pack(fill = BOTH, expand = 1)

            # 7 8 9  
            # 4 5 6  
            # 1 2 3  
            #   0
            #   E
            for row in range(5):
                Grid.rowconfigure(self, row, weight = 1)
            for col in range(3):
                Grid.columnconfigure(self, col, weight = 1)

            ################ FIRST ROW ################
            #7
            img = PhotoImage(file = "Keypad/images/7.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("7"))
            button.image = img
            button.grid(row = 1, column = 0, sticky = N+E+W+S)
            #8
            img = PhotoImage(file = "Keypad/images/8.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("8"))
            button.image = img
            button.grid(row = 1, column = 1, sticky = N+E+W+S)

            #9
            img = PhotoImage(file = "Keypad/images/9.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("9"))
            button.image = img
            button.grid(row = 1, column = 2, sticky = N+E+W+S)

            ################# SECOND ROW #########################
            #4
            img = PhotoImage(file = "Keypad/images/4.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("4"))
            button.image = img
            button.grid(row = 2, column = 0, sticky = N+E+W+S)

            #5
            img = PhotoImage(file = "Keypad/images/5.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("5"))
            button.image = img
            button.grid(row = 2, column = 1, sticky = N+E+W+S)

            #6
            img = PhotoImage(file = "Keypad/images/6.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("6"))
            button.image = img
            button.grid(row = 2, column = 2, sticky = N+E+W+S)

            ################# THIRD ROW #########################

            #1
            img = PhotoImage(file = "Keypad/images/1.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("1"))
            button.image = img
            button.grid(row = 3, column = 0, sticky = N+E+W+S)

            #2
            img = PhotoImage(file = "Keypad/images/2.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("2"))
            button.image = img
            button.grid(row = 3, column = 1, sticky = N+E+W+S)

            #3
            img = PhotoImage(file = "Keypad/images/3.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("3"))
            button.image = img
            button.grid(row = 3, column = 2, sticky = N+E+W+S)

            ################# FOURTH ROW #########################

             #0
            img = PhotoImage(file = "Keypad/images/0.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.process("0"))
            button.image = img
            button.grid(row = 4, column = 1, sticky = N+E+W+S)

            #backspace
            img = PhotoImage(file = "Keypad/images/bak.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.backspace())
            button.image = img
            button.grid(row = 4, column = 0, sticky = N+E+W+S)

            #Enter
            img = PhotoImage(file = "Keypad/images/eql.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.unlock())
            button.image = img
            button.grid(row = 4, column = 2, sticky = N+E+W+S) 

        ##################################################################
        def process(self, button):
            if (button == "AC"):
                self.clearcounter += 1
                self.display["text"] = ""
                self.charactercount = 0
            elif (button == "="):
                try:
                    self.equalscounter += 1
                    expr = self.display["text"]
                    result = eval(expr)
                    self.display["text"] = str(result)

                    # function that truncates any output over the range of 4 
                    lresult = list(str(result))
                    if (len(lresult) >= 4):
                        temp = list(self.display["text"])
                        trunc = ""
                        

                except:
                    self.display["text"] = "ERROR"

            # Else if statement that does not allow buttons to be pressed when character count = 14
            elif(self.charactercount != 4):
                    self.display["text"] += button
                    self.charactercount += 1
                    
                    # if loop that resets display to the pressed button if equals or clear were pressed 
                    if (self.clearcounter == 1 or self.equalscounter == 1):
                        temp = self.display["text"]
                        clearlist = list(temp)
                        length = len(clearlist)
                        for i in range(length - 1):
                            del clearlist[-2]
                        newdisplay = ""
                        newdisplay = newdisplay.join(clearlist)
                        self.display["text"] = newdisplay
                        self.clearcounter = 0 
                        self.equalscounter = 0 
                        self.charactercount = 1

        # Backspace function that deletes the last entered value and decrements the character count accordingly
        def backspace(self):
                temp = self.display["text"] 
                displayList = list(temp)
                length = len(displayList)

                self.display["text"] = temp[:length - 1]
                self.charactercount -= 1

        def unlock(self):
           # if (self.unlocked == True):
               # self.display["text"] = "Locked"
               # GPIO.output(17,False)
               # self.unlocked = False
               # Servo2.lock()
               # GPIO.cleanup()
                
            if (self.display["text"] == str(message)):
                self.process("AC")
                self.display["text"] = "Granted"
                self.unlocked = True
                GPIO.output(17,True)
                Unlock()
                
            else:
                self.process("AC")
                self.display["text"] = "Denied"
                GPIO.cleanup()
                quit()

def StartKeypad():
    #create the window
    keypad = Tk()

    #set the window title
    keypad.title("Keypad")

    #generate the window
    k = Keypad(keypad)

    #display and wait for user interaction
    keypad.mainloop()

############################# END KEYPAD SETUP ###########################################################
                    
############################# SERVO FUNCTIONS ############################################################

servo = GPIO.PWN(12, 50)

def Unlock():
    servo.start(2)
    time.sleep(.5)
    servo.stop()

def Lock():
    servo.start(8)
    time.sleep(.5)
    servo.stop()


############################## END SERVO FUNCTIONS #######################################################

############################## OTHER FUNCTIONS ###########################################################

def Start():
    
    StartKeypad()
    k.display["text"] = "Place tag"
    Id, text = Read()
    if (Id in cards):
        message = random(randint(0,9))
        Email(message, s.textInput)
    else:
        k.display["text"] = "Denied"
        quit()

############################## BEGIN MAIN CODE ###########################################################

cards =[35915910110]


StartTitle()
Start() 

                        
