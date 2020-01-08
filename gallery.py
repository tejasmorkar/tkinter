from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.iconbitmap('./assets/iconbitmap.ico')

my_img1 = ImageTk.PhotoImage(Image.open("./assets/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./assets/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./assets/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("./assets/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("./assets/img5.jpg"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def bck(img_num):
	global my_label
	global button_fowd
	global button_back

	my_label.grid_forget()
	my_label = Label(image=img_list[img_num-1])
	button_fwd = Button(root, text=">>", command=lambda: fwd(img_num+1))
	button_bck = Button(root, text="<<", command=lambda: bck(img_num-1))

	if img_num == 1:
		button_bck = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_bck.grid(row=1, column=0)
	button_fwd.grid(row=1, column=2)

def fwd(img_num):
	global my_label
	global button_fwd
	global button_bck

	my_label.grid_forget()
	my_label = Label(image=img_list[img_num-1])
	button_fwd = Button(root, text=">>", command=lambda: fwd(img_num+1))
	button_bck = Button(root, text="<<", command=lambda: bck(img_num-1))

	if img_num == 5:
		button_fwd = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_bck.grid(row=1, column=0)
	button_fwd.grid(row=1, column=2)


button_bck = Button(root, text="<<", command=bck, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_fwd = Button(root, text=">>", command=lambda: fwd(2))

button_bck.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2)

root.mainloop()
