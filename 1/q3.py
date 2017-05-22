class Calculator():
	"""used for +,-,*,/"""
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a+b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b

x = Calculator()
print x.div(127,4)
print x.div(127,4.0)
print x.div(127.0,4)
print x.add(14,21.26)