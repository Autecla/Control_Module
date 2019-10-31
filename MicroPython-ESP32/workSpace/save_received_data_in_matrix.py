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

rows_count = 2
cols_count = 4

matrix = [[0 for j in range(cols_count)] for k in range(rows_count)]

urtBT = UART(1, 9600)
urtBT.init(9600, bits=8, parity=None, stop=1, tx=2, rx=4)

urtRFID = UART(2, 9600)
urtRFID.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)
 
v_verde = [b'E6672207\r\n', b'CC6D0785\r\n', b'1074FE73\r\n', b'F0F9FF73\r\n']
v_vermelho = [b'1BC1B165\r\n', b'A95798E5\r\n', b'C33A192B\r\n', b'AEC873D5\r\n']
v_amarelo = [b'A13298E5\r\n', b'717B1A2B\r\n', b'744AEEC5\r\n', b'BABA192B\r\n']
v_azul = [b'954FFC45\r\n', b'D157192B\r\n', b'4A1298E5\r\n', b'D5E0F1C5\r\n']

quantidade_acessos = 0

def store_data (data):
      global quantidade_acessos
      row = data[1] - 48
      col = data[3] - 48
      matrix[row][col] = data[4:30] #Limitar o dado para o ID
      
      quantidade_acessos = quantidade_acessos + 1
      print('Matrix:', matrix)
      return True
      

# define the function blocks
def verde(check):
    global quantidade_acessos
    quantidade_acessos = 0
    while check:
        if (urtRFID.any()):
          dados = urtRFID.readline()
          store_data(dados)
          
        if (urtBT.any()):
          btfim = urtBT.readline()
          #print('Dado:', btfim)
          if(btfim == b'fim\r\n'):
            count_verde = 0
            #print('here')
            for i in range(4):
                #print('i: ', i)
                j = 0
                for j in range(4):
                    #print('j: ', j)
                    if(v_verde[j] == matrix[1][i]):
                        count_verde = count_verde + 1
            
            #urtBT.write(count_verde)  
            #print('count_verde: ', count_verde)
            erro_verde = quantidade_acessos - count_verde
            check = False
            
    return (str(count_verde), str(erro_verde))
    
def vermelho(check):
    global quantidade_acessos
    quantidade_acessos = 0
    while check:
        if (urtRFID.any()):
          dados = urtRFID.readline()
          store_data(dados)
          
        if (urtBT.any()):
          btfim = urtBT.readline()
          #print('Dado:', btfim)
          if(btfim == b'fim\r\n'):
            count_vermelho = 0
            #print('here')
            for i in range(4):
                #print('i: ', i)
                j = 0
                for j in range(4):
                    #print('j: ', j)
                    if(v_vermelho[j] == matrix[1][i]):
                        count_vermelho = count_vermelho + 1
            
            #urtBT.write(count_verde)  
            #print('count_vermelho: ', count_vermelho)
            erro_vermelho = quantidade_acessos - count_vermelho
            check = False
            
    return (str(count_vermelho), str(erro_vermelho))
    
def amarelo(check):
    global quantidade_acessos
    quantidade_acessos = 0
    while check:
        if (urtRFID.any()):
          dados = urtRFID.readline()
          store_data(dados)
          
        if (urtBT.any()):
          btfim = urtBT.readline()
          #print('Dado:', btfim)
          if(btfim == b'fim\r\n'):
            count_amarelo = 0
            #print('here')
            for i in range(4):
                #print('i: ', i)
                j = 0
                for j in range(4):
                    #print('j: ', j)
                    if(v_amarelo[j] == matrix[1][i]):
                        count_amarelo = count_amarelo + 1
            
            #urtBT.write(count_verde)  
            #print('count_amarelo: ', count_amarelo)
            erro_amarelo = quantidade_acessos - count_amarelo
            check = False
            
    return (str(count_amarelo), str(erro_amarelo))
    
def azul(check):
    global quantidade_acessos
    quantidade_acessos = 0
    while check:
        if (urtRFID.any()):
          dados = urtRFID.readline()
          store_data(dados)
          
        if (urtBT.any()):
          btfim = urtBT.readline()
          #print('Dado:', btfim)
          if(btfim == b'fim\r\n'):
            count_azul = 0  
            #print('here')
            for i in range(4):
                #print('i: ', i)
                j = 0
                for j in range(4):
                    #print('j: ', j)
                    if(v_azul[j] == matrix[1][i]):
                        count_azul = count_azul + 1
                        
            #urtBT.write(count_verde)  
            #print('count_azul: ', count_azul)
            erro_azul = quantidade_acessos - count_azul
            check = False
            
    return (str(count_azul), str(erro_azul))
    
# map the inputs to the function blocks
options = {b'verde\r\n' : verde,
           b'vermelho\r\n' : vermelho,
           b'amarelo\r\n' : amarelo,
           b'azul\r\n' : azul,
}

while True:
     #This part is to receive data from smartphone
    if (urtBT.any()):
        BTdata = urtBT.readline()
        print('Dado:', BTdata)
        (count, erro) = options[BTdata](True)
        urtBT.write('Acertos: ')
        urtBT.write(count)
        urtBT.write('\n')
        urtBT.write('Erros: ')
        urtBT.write(erro)
        urtBT.write('\n')
        matrix = [[0 for j in range(cols_count)] for k in range(rows_count)]
 
 #   if (urt.any()):
 #       dados = urtRFID.readline()
 #       store_data(dados)

