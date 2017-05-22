class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.l = []
	def enqueue(self,a):
		self.l.insert(0,a)
	def dequeue(self):
		self.l.pop()
	def isEmpty(self):
		s = len(self.l)
		return s==0
	def top(self):
		return self.l[-1]
	def count(self):
		return len(self.l)


a = Queue()
a.enqueue(4)
a.enqueue(5)
a.enqueue(7)
print a.top()
a.dequeue()
print a.count()
print a.isEmpty()
print a.top()
a.dequeue()
a.dequeue()
print a.isEmpty()
