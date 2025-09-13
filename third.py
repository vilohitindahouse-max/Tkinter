from tkinter import *
window = Tk()
window.title("Event handling")
window.geometry("200x200")
def handlekey_press(event):
    print(event.char)
window.bind("<Key>", handlekey_press)
def handlemouse_click(event):
    print("button mouse click")
button = Button(text = "click_me")
button.bind("<Button-1>", handlemouse_click)
button.pack()
window.mainloop()

