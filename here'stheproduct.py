import tkinter as tk

def multiply():
    a = float(e1.get())
    b = float(e2.get())
    result.config(text = a*b)
root = tk.Tk()
e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()
btn = tk.Button(root, text="Multiply", command=multiply)
btn.pack()
result = tk.Label(root, text="")
result.pack()
root.mainloop()