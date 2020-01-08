from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I Clicked a Button")
	myLabel.pack()

myButton = Button(root, text="Click Me", fg="#ffffff", bg="#242424", padx=50, pady=50,  command=myClick)
myButton.pack()

root.mainloop()
