from Tkinter import *
import RPi.GPIO as GPIO
import Servo2



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)

def Gui(message):
    class MainGUI(Frame):
        def __init__(self, parent, equalscounter = 0, clearcounter = 0, charactercount = 0):
            Frame.__init__(self, parent, bg = "white")
        def show(self):
            self.lift()
        

    class FirstGUI(MainGUI):
        def __init__(self, parent, equalscounter = 0, clearcounter = 0, charactercount = 0):
            MainGUI.__init__(self, parent, bg = "white")
            parent.attributes("-fullscreen", True) 
            self.setUpGui()

            self.unlocked = False
            # class variables to track equals, clears, and characters
            self.equalscounter = equalscounter  
            self.clearcounter = clearcounter 
            self.charactercount = charactercount
    
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
            img = Image.PhotoImage(file = "Keypad/images/Welcome.gif")
            image = Image(row = 4, column = 1)
        
            #New User
            img = PhotoImage(file = "Keypad/images/NewUser.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                                activebackground = "white",\
                                command = lambda : self.newUser())
            button.image = img
            button.grid(row = 4, column = 0, sticky = N+E+W+S)

            #Unlock
            img = PhotoImage(file = "Keypad/images/Unlock.gif")
            button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                                activebackground = "white",\
                                command = lambda : self.unlock)
            button.image = img
            button.grid(row = 4, column = 2, sticky = N+E+W+S)

    ##################Window##################
    window = Tk()

    window.title("Keypad")

    p = FirstGUI(window)

    window.mainloop()

    ############################################
    
    class SecondGUI(MainGUI):
        def __init__(self, parent, equalscounter = 0, clearcounter = 0, charactercount = 0):
            MainGUI.__init__(self, parent, bg = "white")
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
                Servo2.unlock()
                
            else:
                self.process("AC")
                self.display["text"] = "Denied"
                GPIO.cleanup()
                quit()
                
    ####################### MAIN CODE ####################################

    #create the window
    window = Tk()

    #set the window title
    window.title("Keypad")

    #generate the window
    p = SecondGUI(window)

    #display and wait for user interaction
    window.mainloop()

    class MainView(Frame):
        def __init__(self, parent, equalscounter = 0, clearcounter = 0, charactercount = 0):
            Frame.__init__(self, parent, bg = "white")
            Title_Screen = FirstGUI(self)
            Keypad = SecondGUI(self)

            buttonframe = Frame(self)
            container = Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)

            Title_Screen.place(in_container, x=0, y=0, relwidth=1, relheight=1)
            Keypad.place(in_container, x=0, y=0, relwidth=1, relheight=1)

            b1 = Button(buttonframe, text="Title Screen", command=Title_Screen.lift)
            b2 = Button(buttonframe, text="Title Screen", command=Keypad.lift)

            b1.pack(side="left")
            b2.pack(side="left")

            Title_Screen.show()

        if __name__ == "__main__":
            root = Tk()
            main = MainView(root)
            main.pack(side="top", fill="both", expand=True)
            root.wm_geometry("400x400")
            root.mainloop()



            
