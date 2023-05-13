from tkinter import *
from time import strftime

digital_clock = Tk()
digital_clock.geometry("600x300")
digital_clock.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p')  # %H = Hour , %M = Minute , %S = Second , %p =am or pm according to the given time value
    lable.config(text = string)
    lable.after(1000,time)

lable = Label(digital_clock, font = ('calibri',40, 'bold'),background= 'black', foreground= 'blue')

lable.pack(anchor= 'center')
time() #function calling

mainloop()
