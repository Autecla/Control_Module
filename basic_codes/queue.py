Nome: Gabriela Alves (@gabialvesr)
#----------Fila----------#
Class Queue:
	def _init_(self):
		self.queue = []
		self.len_queue = 0

	def push(self, x):
		self.queue.append(x)
		self.len_queue += 1

	def pop(self):
		if not self.empty:
			x = self.queue.pop(0)
			self.len_queue -= 1
			return x
		return None
	
	def front(self):
		if not self.empty:
			x = self.queue[0]
			return x
		return None
	def empty(self):
		if (self.len_queue == 0):
			return True
		return False
	def lenght(self):
		return self.len_queue
