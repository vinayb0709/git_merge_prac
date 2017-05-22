class Rectangle():
	"""Rectangle class that returns area and perimeter"""
	def __init__(self,width=None,height=None):
		self.width = width
		self.height = height
	def getArea(self):
		return (self.width * self.height);
	def getPerimeter(self):
		return ( 2 * (self.width + self.height))

x = Rectangle(4,5)
y = Rectangle()
print x.getArea()
y.width = 6
y.height = 7
print y.getPerimeter()