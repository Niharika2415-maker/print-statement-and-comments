from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("200x150")

# Function to handle keypress
def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

# Function to handle button click
def handle_click(event):
    print("\nThe button was clicked")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()