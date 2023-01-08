#Button widget:designed to interact with the user
#A python function can be associated with a button
#This function will be executed, if the button is pressed.
from tkinter import *
class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame,text="Quit",fg="Red",command=quit)
        self.button.pack(side=RIGHT)
        self.slogan=Button(frame,text="Hello",command=self.write_slogan)
        self.slogan.pack(side=RIGHT)
    def write_slogan(self):
        print("Tkinter is easy to use")
root=Tk()
app=App(root)
#root.mainloop()
    
