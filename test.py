from Tkinter import *




from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS import openEMSstim
my_ems_board = openEMSstim.openEMSstim("/dev/tty.usbserial-A9WRN9D1",19200)


def Rock():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
   my_ems_board.send(ems_command(1,var.get(),250))
   my_ems_board.send(ems_command(2,var.get(),250))
def Scissor():
   selection1 = "Value = " + str(var1.get())
   label1.config(text = selection1)
   my_ems_board.send(ems_command(2,var1.get(),500))

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Rock Test", command=Rock)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

var1 = DoubleVar()
scale1 = Scale( root, variable = var1 )
scale1.pack(anchor=CENTER)

button1 = Button(root, text="Scissor Test",command=Scissor)
button1.pack(anchor=CENTER)

label = Label(root)
label.pack()

label1 = Label(root)
label1.pack()

root.mainloop()