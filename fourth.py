from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Event handling")
window.geometry("200x200")
def handlemouse_click(event):
    messagebox.showwarning("Alert", "You are in the message box")
button = Button(text = "click_me")
button.bind("<Button-1>", handlemouse_click)
button.pack()
window.mainloop()

