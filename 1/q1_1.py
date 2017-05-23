class Car():
	"""docstring for Car"""
	def __init__(self,color_name = None,company_name,model_name = None,gear_num = None):
		self.color = color_name
		self.company = company_name
		self.model = model_name
		self.gear = gear_num

	def changeColor(self,new_color):
		self.color = new_color

	def setSpeed(self,new_speed):
		self.speed = new_speed	