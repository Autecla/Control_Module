#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Circular Buffer
#   Sketch/program using micropython to store the data in the Circular Buffer
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************

class CircularBuffer:

    #Constructor
    def __init__(self):
        self.queue = [[] for i in range(4)] #Initializing the list
        self.has_data = [[0] for i in range(4)] #A list to check if the position data is available for a new data
        self.head = 0
        self.tail = 0
        self.maxSize = 4 #TAM_BUFFER

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

#Testing the buffer operation  
i = 0;
buffer_data = CircularBuffer()
buffer_data.print_queue()

for i in range(4):
  buffer_data.enqueue(i)
  buffer_data.print_queue()
  buffer_data.print_has_data()
  buffer_data.print_head()
  buffer_data.print_tail()
  print('Size:', buffer_data.size())

for i in range(4):
  x = buffer_data.dequeue()
  print('data:', x)
  buffer_data.print_queue()
  buffer_data.print_has_data()
  buffer_data.print_head()
  buffer_data.print_tail()
  print('Size:', buffer_data.size())

for i in range(2):
  buffer_data.enqueue(i+9)
  buffer_data.print_queue()
  buffer_data.print_has_data()
  buffer_data.print_head()
  buffer_data.print_tail()
  print('Size:', buffer_data.size())
  

print('Fila Final:')
buffer_data.print_queue()

