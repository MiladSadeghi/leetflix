import json 
import requests
import subprocess
from tkinter import *

def geo(window,x,y):
    scr_width, scr_height = window.winfo_screenwidth(), window.winfo_screenheight()
    scr_x, scr_y = (scr_width/2) - (x/2), (scr_height/2) - (y/2)
    x = '%dx%d+%d+%d' % (x, y, scr_x, scr_y)
    return x

#window
win = Tk()
win.title('LEETFLIX')
win.geometry(geo(win, 350, 400))
win.resizable(FALSE, FALSE)

#enter movie name
movieName_label = Label(win, text='Movie name (or Keywords)', font=('',9))
movieName_entry = Entry(win, width=30, font=('',13), justify=CENTER)
movieName_label.place(x = 30, y = 20)
movieName_entry.place(x = 33, y = 47)

win.mainloop()