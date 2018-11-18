#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Receive from UART_serial
#   Sketch/program to read data from RFID_Module by UART_serial using micropython
#   ESP32 Port:
#     Pin_RX = 16
#     Pin_TX = 17
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************/

from machine import UART
import time
import _thread
import threading


class CircularBuffer:

    #Constructor
    def __init__(self):
        self.queue = ['0' for i in range(10)] #Initializing the list
        self.has_data = ['0' for i in range(10)] #A list to check if the position data is available for a new data
        self.head = 0
        self.tail = 0
        self.maxSize = 10 #TAM_BUFFER

    #Adding elements to the queue
    def enqueue(self, data):
        #if (self.size() == self.maxSize-1):
        #    return ("Queue Full! Back to the beginning of the queue!")
        print('has_data:', self.has_data[self.tail])
        if (self.has_data[self.tail] == '0'): 
            print('here')
            self.queue[self.tail] = data
            self.has_data[self.tail] = 1
            self.tail = (self.tail + 1) % self.maxSize
            return True

    #Removing elements from the queue
    def dequeue(self):
        if (self.has_data[self.head] == 0):
            return ("Queue Empty!") 
        if (self.has_data[self.head] == 1):
            data = self.queue[self.head]
            self.has_data[self.head] = 0
            self.head = (self.head + 1) % self.maxSize
            return data

    #Calculating the size of the queue
    def size(self):
        if (self.tail>=self.head):
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))
    
    #Printing the queue information
    def print_queue(self):
        print('Fila:', self.queue)
        return True
        
    def print_has_data(self):
        print('Has_data[]:', self.has_data)
        return True
        
    def print_head(self):
        print('Head:', self.head)
        return True
        
    def print_tail(self):
        print('Tail:', self.tail)
        return True
        

def get_data_from_rfid (check, dados):
        if(check):
          buffer_data.enqueue(dados)
        
#    print('Buffer:')
#    buffer_data.print_queue()

#init matrix
rows_count = 7
cols_count = 7
matrix = [[0 for c in range(cols_count)] for r in range(rows_count)]

def store_data (check, i):
    #print('oi')
    if(check):
        while check:
            if(buffer_data.has_data[buffer_data.head]):
                print('store')
                data = buffer_data.dequeue()
                #print('Data:', data)
                row = data[1] - 48
                #print('row:', row)
                col = data[3] - 48
                #print('col:', col)
                matrix[row][col] = data[4:30]
                arq = matrix[row][col]
                file = open("Matrix.txt","a")
                file.write(arq)
                file.write('\n')
                file.close()
                time.sleep(0.25)
                i = i + 1
                if(i == 5):
                    check = False
        
        print('Matrix:')#, matrix)
        return True

urt = UART(2, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

#init buffer
buffer_data = CircularBuffer()


while True:
  if (urt.any()):
    dados = urt.readline()
    print('Dado:', dados)
    #_thread.start_new_thread(get_data_from_rfid, (True, dados))
    #_thread.start_new_thread(store_data, (True, 0))
    t1 = threading.Thread(target=get_data_from_rfid, args=(True, dados))
    t1.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
    t1.start()
    
    t2 = threading.Thread(target=store_data, args=(True, 0))
    t2.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
    t2.start()
    #buffer_data.print_queue()
    #print('Size:', buffer_data.size())
    #if(buffer_data.size() == 6):
    #    store_data()   


