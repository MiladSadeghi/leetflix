import json
from tkinter.messagebox import *
import requests
import subprocess
from tkinter import *
from tkinter import ttk

#api
API_URL = "https://leetflix.haghiri75.com"

#position app
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


rootFrame = Frame(win)
rootFrame.grid(padx=37, pady=(13,0))

#enter movie name
movieName_label = Label(rootFrame, text='Movie name (or Keywords)', font=('',9))
movieName_entry = Entry(rootFrame, width=30, font=('',13), justify=CENTER)
movieName_label.grid(sticky=W, pady=(0,10))
movieName_entry.grid(pady=(0,10), ipady=2)

#button Find!
findMovie_button = Button(rootFrame ,text='Find', width=38, command=findCommand)
findMovie_button.grid(pady=(0,14))

#table for movie list
movielist_table = ttk.Treeview(rootFrame, show='headings', columns=(0))
movielist_table.grid()
movielist_table.column(0, width=275, stretch=NO, anchor="center")
movielist_table.heading(0, text='Movies', anchor=W)

#download button
downloadButton = Button(rootFrame, text='Download', width=38)
downloadButton.grid(pady=(10,0))

win.mainloop()
