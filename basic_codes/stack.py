Nome: Gabriela Alves (@gabialvesr)
#----------Pilha----------#
Class Stack:
	def _init_(self):
		self.stack = []
		self.len_stack = 0

	def push(self, x):
		self.stack.append(x)
		self.len_stack += 1

	def pop(self):
		if not self.empty:
			x = self.stack.pop(len_stack)
			self.len_stack -= 1
			return x
		return None
	
	def top(self):
		if not self.empty:
			x = self.stack[-1]
			return x
		return None
	def empty(self):
		if (self.len_stack == 0):
			return True
		return False
	def lenght(self):
		return self.len_stack