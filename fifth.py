import tkinter 
from tkinter import messagebox
window = tkinter.Tk()
window.title("Messagebox program")
window.geometry("500x400")
main_heading = tkinter.Label(text = "Hey there!", fg = "white", bg = "black", height = 1, width = 30)
main_heading.pack(pady = 20)
namelabel = tkinter.Label(text = "full name")
namelabel.pack()
nameentry = tkinter.Entry()
nameentry.pack()
def displayname():
    name = nameentry.get()
    global message
    greet = "Hello " + name
    textbox.insert(tkinter.END, greet)
    messagebox.showwarning("Alert", greet)
textbox = tkinter.Text(window,height = 5, width = 40)
clickbutton = tkinter.Button(window,text = "begin", command = displayname, height = 1, width = 15)
textbox.pack(pady = 10)
clickbutton.pack(pady = 10)
window.mainloop()