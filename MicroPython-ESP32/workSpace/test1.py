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
from time import sleep

urtBT = UART(1, 9600)
urtBT.init(9600, bits=8, parity=None, stop=1, tx=2, rx=4)

urtRFID = UART(2, 9600)
urtRFID.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

rows_count = 1
cols_count = 6
aux_activity = [[0 for j in range(cols_count)] for k in range(rows_count)]

def store_data (data):
  global quantidade_acessos
  global aux_activity
  
  tags = data.split('%')
  num_tags = len(tags)
  row = tags[0][-1:]
  
  for i in range(1, num_tags):
    aux_activity[row][i] = data #Limitar o dado para o ID
  
  print('Matrix:', aux_activity)
  return True


def during_activity(check, activity):
  global aux_activity
  global quantidade_acessos
  quantidade_acessos = 0 # lembrar de contar quantas cartas a criança colocou

  print("PRONTO PRA COMEÇAR A ATIVIDADE", activity)
  while check:
    if (urtRFID.any()):
      data = urtRFID.readline()
      store_data(data)
      print('Dado:', dados)
    
    if (urtBT.any()):
      btfim = urtBT.readline()
      if(btfim == b'fim\r\n'):
        print("FIM")
        check = False
        
  return (aux_activity)

options = {b'cores\r\n' : 0,
           b'sequencia\r\n' : 1,
}

#print("Aux:")
#print(aux_activity)
#print("\n")
while True:
  #This part is to receive data from smartphone
  #print ("teste: ")
  #sleep(0.5) 
  count = 0
  if (urtBT.any()):
    BTdata = urtBT.readline()
    print('Dado:', BTdata)
    activity, count_acertos, erro_activity = during_activity(True, options[BTdata])
    count +=count
    urtBT.write('Atividade: ')
    urtBT.write(activity)
    urtBT.write('\r')
    urtBT.write(' Acertos: ')
    urtBT.write(count_acertos)
    urtBT.write('\r')
    urtBT.write(' Erros: ')
    urtBT.write(erro_activity)
    urtBT.write('\r\n')


