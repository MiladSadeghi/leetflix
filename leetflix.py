import json 
import requests
import subprocess
from tkinter import *

def geo(window,x,y):
    scr_width, scr_height = window.winfo_screenwidth(), window.winfo_screenheight()
    scr_x, scr_y = (scr_width/2) - (x/2), (scr_height/2) - (y/2)
    x = "%dx%d+%d+%d" % (x, y, scr_x, scr_y)
    return x

#window
win = Tk()
win.title('LEETFLIX')
win.geometry(geo(win, 350, 400))
win.resizable(FALSE, FALSE)

# """highlightbackground="black", highlightthickness=1"""
test = Frame(win)
test.grid(padx=37, pady=(20,0))

#enter movie name
movieName_label = Label(test, text='Movie name (or Keywords)', font=('',9))
movieName_entry = Entry(test, width=30, font=('',13), justify=CENTER)
movieName_label.grid(sticky=W, pady=(0,10))
movieName_entry.grid(pady=(0,10), ipady=2)

#button Find!
findMovie_button = Button(test ,text='Find', width=38)
findMovie_button.grid(pady=(0,14))

#text area for movie list
movielist_text = Text(test, width=34, height=13)
movielist_text.grid()

win.mainloop()
