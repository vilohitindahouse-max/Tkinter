from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("1000x1000")
upload = Image.open("app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root,image=image,bg = "light grey")
label.place(x=180, y = 20)
label1 = Label(root, text="Hey user, welcome to denomination counter",bg ="light grey" )
label1.place(x=0.5,y  = 340, anchor=CENTER)
def message():
    Messagebox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count")
    if Messagebox == "okay":
        topwin()
button = Button(root, text = "Let's get started", command = message, bg = "light grey", fg = "Red")
def topwin(): 
    top = Toplevel()
    top.title("Denomination calculator")
    top.config(bg = "light grey")
    top.geometry("600x350+50+50")
    label = Label(top, text = "enter total amount",bg = "light grey")
    entry = Entry(top)
    lbl = Label(top,text="There a number of notes for each denominator", bg = "light grey")
    l1 = Label(top,text="100", bg = "light grey")
    l2 = Label(top,text="10", bg = "light grey")
    l3 = Label(top,text="5", bg = "light grey")
    l4 = Label(top,text="1", bg = "light grey")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note_100 = amount // 100
            amount %=100
            note_10 = amount // 10
            amount %= 10
            note_5 = amount // 5
            amount %= 5
            note_1 = amount // 1
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t1.insert(END,str(note_100))
            t2.insert(END,str(note_10))
            t3.insert(END,str(note_5))
            t4.insert(END,str(note_1))
        except ValueError:
            messagebox.showerror("error", "Please enter a valid number.")
    btn = Button(top, text = "Calculate", command = calculate, bg="brown", fg = "white")
    label.place(x = 1000, y = 50)
    entry.place(x = 200, y = 80)
    btn.place(x = 240, y = 120) 
    lbl.place(x = 140, y = 170)
    l1.place(x = 180, y = 200)
    l2.place(x = 180, y =230)
    l3.place(x = 180, y = 260)
    l4.place(x = 180, y = 290)
    t1.ploce(x = 270, y = 200)
    t2.place(x = 270, y = 230)
    t3.place(x = 270, y = 260)
    t4.place(x = 270, y = 290)
    top.mainloop()
root.mainloop()




    

    
