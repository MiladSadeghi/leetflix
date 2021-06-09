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
win.geometry(geo(win, 350, 420))
win.resizable(0, 0)

#get from api
def getData():
    movielist_table.delete(*movielist_table.get_children())
    movielist_table.insert('', END)
    response = requests.post(API_URL, data=json.dumps({"keyword" : movieName_entry.get()}), headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0', 'content-type': 'application/json'})
    response = json.loads(response.text)
    return response

#command button find
def findButton_Command():
    data = getData()
    if len(data) == 0:
        return showerror('Error!', 'Nothing found!')
    index = 1
    for result in data:
        movielist_table.insert('', END, text='', values=(index, f"""{result["title"]}"""))
        index += 1

#frame
rootFrame = Frame(win)
rootFrame.pack(padx=37, pady=(13,0))

#enter movie name
movieName_label = Label(rootFrame, text='Movie name (or Keywords)', font=('',9))
movieName_entry = Entry(rootFrame, width=30, font=('',13), justify=CENTER)
movieName_label.pack(pady=(0,10))
movieName_entry.pack(pady=(0,10), ipady=2)

#button Find!
findMovie_button = Button(rootFrame ,text='Find', width=38, command=findButton_Command)
findMovie_button.pack(pady=(0,14))

#table for movie list
tableFrame = Frame(rootFrame)

movielist_table = ttk.Treeview(tableFrame, show='headings', columns=('id','name'))
verscrlbar = Scrollbar(tableFrame, orient = HORIZONTAL, command = movielist_table.xview)
movielist_table.configure(xscrollcommand = verscrlbar.set)
verscrlbar.pack(side = 'bottom', fill = X)
movielist_table.pack()
tableFrame.pack()

movielist_table.column('id', width=20, anchor=W, stretch=FALSE)
movielist_table.column('name', width = 415, anchor=W, stretch=FALSE)

movielist_table.heading('id', text='ID', anchor=CENTER)
movielist_table.heading('name', text='Movie Name', anchor=W)

#download button
downloadButton = Button(rootFrame, text='Download', width=38)
downloadButton.pack(pady=(13,0))

win.mainloop()
