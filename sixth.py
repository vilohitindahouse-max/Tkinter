from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Codingal's text editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800, weight = 1)
window.columnconfigure(1,minsize=800, weight = 1)
def openfile():
    filepath = askopenfilename(filetypes=[("text files", "*.txt" ), ("All files", "*.*")])
    if not filepath:
        return
    textedit.delete(1.0, END)
    with open(filepath, "r") as inputfile:
        text = inputfile.read()
        textedit.insert(END, text)
        inputfile.close()
    window.title(f"Codingal's text editor -{filepath} ")
def savefile():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("text files", "*.txt" ), ("All files", "*.*")])
    if not filepath:
        return
    with open(filepath,"W") as outputfile:
        text = textedit.git(1.0,END)
        outputfile.write(text)
    window.tile(f"Codingal's text editor -{filepath}")
textedit = Text(window)
fr_button=Frame(window, relief=RAISED, bd = 2)
buttonopen = Button(fr_button, text = "Open", command = openfile)
buttonsave = Button(fr_button,text = "save", command = savefile )
buttonopen.grid(row = 0, column = 0, sticky = "ew", padx=5, pady = 5)
buttonsave.grid(row = 1, column = 0, sticky = "ew", padx=5,)
fr_button.grid(row=0, column=0,sticky="ns")
textedit.grid(row = 0, column=1, sticky = "nsew")
window.mainloop()

