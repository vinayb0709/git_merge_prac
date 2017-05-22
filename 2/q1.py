class Stack():
	"""docstring for Stack"""
	def __init__(self):
		self.l = []
	def push(self,a):
		self.l.append(a)
	def pop(self):
		self.l.pop()
	def isEmpty(self):
		s = len(self.l)
		return s==0
	def top(self):
		return self.l[-1]
	def count(self):
		return len(self.l)


a = Stack()
a.push(4)
a.push(5)
a.push(7)
print a.top()
a.pop()
print a.count()
print a.isEmpty()
print a.top()
a.pop()
a.pop()
print a.isEmpty()
