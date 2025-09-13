from tkinter import *
import datetime
window = tkinter.Tk()
window.title("My first Tkinter program")
window.geometry("500x400")
main_heading = tkinter.Label(text = "Frame widget", fg = "white", bg = "black", height = 1, width = 30)
main_heading.pack(pady = 20)
bordereffect = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]
window.mainloop()