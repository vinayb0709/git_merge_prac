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

class Queue_using_Stack(object):
	"""docstring for Queue_using_Stack"""
	def __init__(self):
		self.a = Stack()
	def enqueue(self,s):
		b = Stack()
		while (not self.a.isEmpty()):
			t = self.a.top()
			self.a.pop()
			b.push(t)
		self.a.push(s)
		while (not b.isEmpty()):
			t = b.top()
			b.pop()
			self.a.push(t)
	def dequeue(self):
		t = self.a.top()
		self.a.pop()
		return t
	def isEmpty(self):
		return self.a.isEmpty()
	def getFirst(self):
		return self.a.top()
	def getLast(self):
		b = Stack()
		while not self.a.isEmpty():
			t = self.a.top()
			self.a.pop()
			b.push(t)
		r = b.top()
		while not b.isEmpty():
			t = b.top()
			b.pop()
			self.a.push(t)
		return r


b = Queue_using_Stack()
b.enqueue(4)
b.enqueue(5)
b.enqueue(7)
print b.getFirst()
print b.getLast()
print b.dequeue()
print b.isEmpty()
print b.dequeue()
print b.dequeue()
print b.isEmpty()
