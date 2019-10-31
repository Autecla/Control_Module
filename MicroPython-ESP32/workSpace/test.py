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
from machine import Pin
led=Pin(27,Pin.OUT)  
ledone = Pin(25,Pin.OUT)
rows_count = 1
cols_count = 6

aux_activity = [[0 for j in range(cols_count)] for k in range(rows_count)]

urtBT = UART(1, 9600)
urtBT.init(9600, bits=8, parity=None, stop=1, tx=2, rx=4)

urtRFID = UART(2, 9600)
urtRFID.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

activities = [[b'954FFC45\r\n', b'D157192B\r\n', b'4A1298E5\r\n', b'D5E0F1C5\r\n', b'A13298E5\r\n', b'717B1A2B\r\n']]

quantidade_acessos = 0
tot_activity = 0

def check_activity(id_activity, quant_access):
  global rows_count
  global cols_count
  
  temp_activity = [[0 for j in range(cols_count)] for k in range(rows_count)]
  count_acertos = 0
  temp_activity[0][0:] = activities[id_activity]
  for j in range(6):
      if(temp_activity[id_activity][j] == aux_activity[id_activity][j]):
        count_acertos = count_acertos + 1
  
  erro_activity = quant_access - count_acertos
  return(str(count_acertos), str(erro_activity))


def store_data (data):
  global quantidade_acessos
  global aux_activity
  
  row = data[1] - 48
  col = data[3] - 48
  aux_activity[row][col] = data[4:30] #Limitar o dado para o ID
  
  quantidade_acessos = quantidade_acessos + 1
  print('Matrix:', aux_activity)
  return True


def during_activity(check, activity):
  global quantidade_acessos
  quantidade_acessos = 0
  print("PRONTO PRA COMEÇAR A ATIVIDADE")
  while check:
    if (urtRFID.any()):
      dados = urtRFID.readline()
      store_data(dados)
      print('Dado:', dados)
      print("RECEBI")
    
    if (urtBT.any()):
      btfim = urtBT.readline()
      if(btfim == b'fim\r\n'):
        print("FIM")
        count_acertos, erro_activity = check_activity(activity, quantidade_acessos)
        check = False
        
  return (str(activity), str(count_acertos), str(erro_activity))

options = {b'cores\r\n' : 0,
           b'sequencia\r\n' : 1,
}

print("Aux:")
print(aux_activity)
print("\n")
while True:
   #This part is to receive data from smartphone
  #print ("teste: ")
  #sleep(0.5) 
  count = 0
  if (urtBT.any()):
    BTdata = urtBT.readline()
    print('Dado:', BTdata)
    if(BTdata == b'fim\r\n'):
        if(count == 0):
          print("FIM")
          count_acertos, erro_activity = str(3), str(1)
          for i in range(3):
            led.value(1)            #Set led turn on
            time.sleep(0.5)
            led.value(0)            #Set led turn off
            time.sleep(0.5)
          led.value(0)
          check = False
        if(count == 1):
          print("FIM")
          count_acertos, erro_activity = str(4), str(0)
          for i in range(3):
            ledone.value(1)            #Set led turn on
            time.sleep(0.5)
            ledone.value(0)            #Set led turn off
            time.sleep(0.5)
          ledone.value(0)
          check = False
        if(count == 2):
          print("FIM")
          count_acertos, erro_activity = str(2), str(2)
          for i in range(3):
            led.value(1)            #Set led turn on
            time.sleep(0.5)
            led.value(0)            #Set led turn off
            time.sleep(0.5)
          led.value(0)
          check = False
        if(count == 3):
          print("FIM")
          count_acertos, erro_activity = str(4), str(0)
          for i in range(3):
            ledone.value(1)            #Set led turn on
            time.sleep(0.5)
            ledone.value(0)            #Set led turn off
            time.sleep(0.5)
          ledone.value(0)
          count = 0
          check = False
    
    count +=count
    urtBT.write(' Acertos: ')
    urtBT.write(count_acertos)
    urtBT.write('\r')
    urtBT.write(' Erros: ')
    urtBT.write(erro_activity)
    urtBT.write('\r\n')
