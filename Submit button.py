from Tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.label = Label(master, text = "Enter email")
        self.label.pack(side = LEFT)
        self.entry = Entry(master)
        self.entry.pack(side = LEFT)
        self.button1 = Button(master, text = "Submit",command = self.Write)
        self.button1.pack(side = LEFT)

    def Write(self):
        print "place tag"
        cards.append(Id)
        
######################################################################


window = Tk()
app = App(window)
window.mainloop()
