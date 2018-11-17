#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Receive data from APP
#   Sketch/program receive data from APP using an external Bluetooth connected on UART(1) and make a .txt with a matrix TAGs
#   Tip: To test this program, you can use Bluetooth terminal on your smartphone to connect to HC-06
#
#   APP: Bluetooth terminal
#
#   ESP32 <--> BT HC-06
#   Ports:
#      Pin_RX = TX2
#      Pin_TX = RX2
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************

import _thread
import time
from machine import UART

urt = UART(1, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=2, rx=4)
i = True
while i:
    dados = urt.write('.')
    #print('Dado:', dados)
    time.sleep(1)

    #Espera matriz de tags
    if (urt.any()):
      dados = urt.readline()
      print('TAGs:', dados)
      i = False

def WriteTXT_thread(check, a):
  while check:
    #print("Hello")
    file = open("Matrix.txt","w")
    file.write(a)
    file.close()
    time.sleep(2)
    #print("from thread")
    check = False


_thread.start_new_thread(WriteTXT_thread, (True, dados))
