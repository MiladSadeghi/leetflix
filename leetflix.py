import json 
import requests
import subprocess
from tkinter import *

def geo(window,x,y):
    scr_width, scr_height = window.winfo_screenwidth(), window.winfo_screenheight()
    scr_x, scr_y = (scr_width/2) - (x/2), (scr_height/2) - (y/2)
    x = '%dx%d+%d+%d' % (x, y, scr_x, scr_y)
    return x

win = Tk()
win.title('LEETFLIX')
win.geometry(geo(win, 400, 400))
win.resizable(FALSE, FALSE)


win.mainloop()