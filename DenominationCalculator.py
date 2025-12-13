from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
root= Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")
try:
    upload= Image.open("img.jpg")
    upload= upload.resize(300,300)
    image= ImageTk.PhotoImage(upload)
    label= Label(root,image=image,bg="light blue")
    label.place(x=180,y=20)
except:
    pass
label1=label(root,text="hey user! Welcome to denomination counter application.",bg="light blue",font=("Arial0",11,"bold"))
label1.place(relx=0.5, y=30, anchor=CENTER)
def msg():
    MsgBox= messagebox.askokcance("ALERT","do you want to calculatee the denomination count?")
    if MsgBox:
        topwin()
button1.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label= Label(top,texxt="enter total amount",bg="light grey")
    label.place(x=220,y=50)
    entry= Entry(top)
    entry.place(x=220,y=80)
    lbl=Label(top,text="here are the number of notes for each denomination",bg="light grey")
lbl.place(x= 140, y=170)
l1= Label(top, text="2000:", bg="light grey")
l2= Label(top, text="500:", bg="light grey")
l3= Label(top, text="100:", bg="light grey")

l1.place(x=180, y=200)
l2.place(x=180,y= 230)
l3.place(x=180,y=260)
t1= Entry(top)
t2= Entry(top)
t3= Entry(top)

t1.place(x=270,y=200)
t2.place(x=270,y=230)
t3.place(x=270,y=260)

def calculator():
    try:
        amount= int(entry.get())
        note2000= amount//2000
        amount%=2000

        note500= amount//500
        amount%= 500

        note100=amount//100
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)

        t1.insert(END,str(note2000))
        t2.insert(END,str(note500))
        t3.insert(END,str(note100))

    except ValueError:
        messagebox.showerror("Error","please enter a valid number.")
btn=Button(top,text="calculate",command="calculator",bg="brown",fg= "white")
btn.place(x=240, y=120)

root.mainloop()
