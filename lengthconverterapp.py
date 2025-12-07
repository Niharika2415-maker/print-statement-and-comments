import tkinter as tk

def convert():
    lbl['text'] = float(ent.get()) * 2.54

root = tk.Tk()
ent = tk.Entry(root); ent.pack()
tk.Button(root, text="Convert", command=convert).pack()
lbl = tk.Label(root, text=""); lbl.pack()
root.mainloop()