#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Receive from UART_serial and store in buffer
#   Sketch/program using micropython to read data from RFID_Module by UART_serial and store the received data in the Circular Buffer
#   Tip: To test this program, you can use an arduino and the program found in "Arduino/test_serial_arduino"
#   ESP32 Port:
#       Pin_RX = 16
#       Pin_TX = 17
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************

from machine import UART

class CircularBuffer:

    #Constructor
    def __init__(self):
        self.queue = [[] for i in range(50)] #Initializing the list
        self.has_data = [[0] for i in range(50)] #A list to check if the position data is available for a new data
        self.head = 0
        self.tail = 0
        self.maxSize = 50 #TAM_BUFFER

    #Adding elements to the queue
    def enqueue(self, data):
        #print('hey:', self.has_data[self.tail])
        #if (self.size() == self.maxSize-1):
        #    return ("Queue Full! Back to the beginning of the queue!")
        #if (self.has_data[self.tail] == '0'): #Doesn't work
        #print('here')
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
        

urt = UART(2, 9600)
urt.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)
buffer_data = CircularBuffer()

while True:
  if (urt.any()):
    dados = urt.readline()
    print('Dado:', dados)
    buffer_data.enqueue(dados)
    print('Buffer:')
    buffer_data.print_queue()
