#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Send data to APP
#   Sketch/program to send data from Control_Module to APP using an external Bluetooth connected on UART(1)
#   Tip: To test this program, you can use Bluetooth terminal on your smartphone to connect to HC-06
#
#   ESP32 <--> BT HC-06
#   Ports:
#      Pin_RX = TX1 = Pin 2
#      Pin_TX = RX1 = Pin 4
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************



from machine import UART
import time

urt = UART(1, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=2, rx=4)
while True:
    urt.write('o')
    time.sleep(1)

    #This part is to receive data from smartphone
    if (urt.any()):
      dados = urt.readline()
      print('Dado:', dados)

