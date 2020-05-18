from Tkinter import *


class FirstGUI(Frame):
    def __init__(self, parent, equalscounter = 0, clearcounter = 0, charactercount = 0):
        Frame.__init__(self, parent, bg = "white")
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
        
        
        #New User
        img = PhotoImage(file = "Keypad/images/NewUser.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white",\
                            command = lambda : self.NewUser())
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
