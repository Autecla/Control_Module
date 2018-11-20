#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Receive from UART_serial and store in a matrix
#   Sketch/program using micropython to read data from RFID_Module by UART_serial and store the received data in a matrix
#   Tip: To test this program, you can use an arduino and the program found in "Arduino/test_serial_arduino"
#   ESP32 Port:
#       Pin_RX = 16
#       Pin_TX = 17
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************

from machine import UART

rows_count = 7
cols_count = 7

matrix = [[0 for j in range(cols_count)] for k in range(rows_count)]


def store_data (data):
      row = data[1] - 48
      col = data[3] - 48
      matrix[row][col] = data[4:30] #Limitar o dado para o ID
      
      
      print('Matrix:', matrix)
      return True
    

urt = UART(2, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

while True:
    if (urt.any()):
        dados = urt.readline()
        store_data(dados)



