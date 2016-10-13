import serial
from time import sleep
from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
#ems_command(_channel, _intensity, _duration):

 
bluetoothSerial = serial.Serial("/dev/tty.Bluetooth-Incoming-Port", 9600 )

while 1:
    # choice = int(raw_input("1 or 2? EMS with full intensity on that channel for 2 seconds"))
    # bluetoothSerial.write(ems_command(choice,100,2000))
    bluetoothSerial.write('fuck\n')

