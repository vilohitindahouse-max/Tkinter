import tkinter
import datetime
window = tkinter.Tk()
window.title("My first Tkinter program")
window.geometry("500x200")
main_heading = tkinter.Label(text = "Hey there!", fg = "white", bg = "black", height = 1, width = 300)
main_heading.pack(pady = 20)
namelabel = tkinter.Label(text = "full name")
namelabel.pack()
nameentry = tkinter.Entry()
nameentry.pack()
def displayname():
    name = nameentry.get()
    global message
    message = "Welcome to application, today's day is"
    greet = "Hello" + name
    textbox.insert(tkinter.END, greet)
    textbox.insert(tkinter.END, message)
    textbox.insert(tkinter.END, datetime.today())
textbox = tkinter.Text(height = 5)
clickbutton = tkinter.Button(window,text = "begin", command = displayname, height = 1, width = 10)
textbox.pack(pady = 10)
clickbutton.pack(pady = 10)
window.mainloop()