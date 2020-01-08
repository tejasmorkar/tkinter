from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="white", bg="#242424")
e.pack()
e.insert(0, "Enter your name")

def myClick():
	myLabel = Label(root, text="Hello {}".format(e.get()))
	myLabel.pack()

myButton = Button(root, text="Submit", fg="#ffffff", bg="#242424", padx=50, pady=50,  command=myClick)
myButton.pack()

root.mainloop()
