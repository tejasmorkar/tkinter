from tkinter import *

root = Tk()
root.title("Simple Calculator")
# root.configure(bg="#242424")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_num = e.get()
	global f_num
	f_num = int(first_num)
	global math
	math = "add"
	e.delete(0, END)

def button_sub():
	first_num = e.get()
	global f_num
	f_num = int(first_num)
	global math
	math = "sub"
	e.delete(0, END)

def button_mul():
	first_num = e.get()
	global f_num
	f_num = int(first_num)
	global math
	math = "mul"
	e.delete(0, END)

def button_div():
	first_num = e.get()
	global f_num
	f_num = int(first_num)
	global math
	math = "div"
	e.delete(0, END)

def button_equal():
	second_num = e.get()
	e.delete(0, END)

	if math == "add":
		e.insert(0, f_num + int(second_num))

	if math == "sub":
		e.insert(0, f_num - int(second_num))

	if math == "mul":
		e.insert(0, f_num * int(second_num))

	if math == "div":
		e.insert(0, f_num / int(second_num))

button_1 = Button(root, bg="#242424", fg="white", text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, bg="#242424", fg="white", text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, bg="#242424", fg="white", text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, bg="#242424", fg="white", text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, bg="#242424", fg="white", text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, bg="#242424", fg="white", text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, bg="#242424", fg="white", text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, bg="#242424", fg="white", text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, bg="#242424", fg="white", text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, bg="#242424", fg="white", text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, bg="#242424", fg="white", text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, bg="#242424", fg="white", text="-", padx=39, pady=20, command=button_sub)
button_mul = Button(root, bg="#242424", fg="white", text="*", padx=40, pady=20, command=button_mul)
button_div = Button(root, bg="#242424", fg="white", text="/", padx=40, pady=20, command=button_div)
button_equal = Button(root, bg="#242424", fg="white", text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, bg="#242424", fg="white", text="Clear", padx=79, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=4, column=1)
button_div.grid(row=4, column=2)

button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()