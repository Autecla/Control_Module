#Nome: Gabriela Alves (@gabialvesr)
Class HashTable:
	def _init_(self,table_size):
		self.table_size = table_size
		self.table = [[] for i in range(table_size)]
	
	def hash_funct(self, x):
		return (x % self.table_size)

	def insert(self, x):
		self.table[self.hash_funct(x)].append(x)

	def search(self,x):
		if x in self.table[self.hash_funct(x)]:
			return True
		return False
