from Tkinter import *
import ttk
from PIL import Image, ImageTk
from random import randint #randint(x,y)

from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS import openEMSstim
my_ems_board = openEMSstim.openEMSstim("/dev/tty.usbserial-A9WRN9D1",19200)

def space(h):
	frame = Label(win, height = h)
	frame.pack()
def wait():
	t.pack_forget()
	easy.pack_forget()
	hard.pack_forget()
	global label 
	label = Label(win)
	label.after(500, rock)

	

def rock():	
	label.pack()
	label.configure(text="Rock!", height=2, font=("Kokonor", 105), fg = "#00A8E8")

	label.after(1200,paper)
def paper():	
	label.configure(text="Paper!", fg='#007EA7' )
	label.after(1200,scissor)
def scissor():
	label.configure(text="Scissors!", fg='#005491')
	rand_number = randint(1, 3)
	print rand_number
	if rand_number == 1:
		my_ems_board.send(ems_command(1,100,1000))

	elif rand_number ==2:
		my_ems_board.send(ems_command(1,100,1000))
		my_ems_board.send(ems_command(2,100,1000))
	else:
		pass
	label.after(3000,go)
def go():
	label.pack_forget()
	t.pack()
	#space(3)
	easy.pack()
	#space(2)
	hard.pack()




win=Tk()
win.title("Rock Paper Scissors")
#win.configure(background = "blue")
#win.resizable(width=False, height=False)
#win.attributes('-fullscreen', True)
win.minsize(1200,900)


image = Image.open("photo/title1.jpg")
image = image.resize( (1300, 700), Image.BILINEAR )
photo = ImageTk.PhotoImage(image)
t = Label(image=photo)
t.image = photo 
t.pack()
#space(3)
#
"""
gra = Image.open("rock.jpg")
gra = image.resize( (400, 400), Image.BILINEAR )
photo1 = ImageTk.PhotoImage(gra)
t1 = Label(image=photo1)
t1.image = photo1
"""



style = ttk.Style()
style.map("TButton",
    foreground=[('pressed', 'blue'), ('active', 'red')],
    )
style.configure('TButton', font=("Kokonor", 25), padding=0, background="#413C58", relief=FLAT)
#style.configure("color.TButton", background="red")

easy = ttk.Button(text="Easy", style="TButton",command = wait)
easy.pack()
#space(2)
hard = ttk.Button(text="Hard", style="TButton",command = wait)
hard.pack()



win.mainloop()
