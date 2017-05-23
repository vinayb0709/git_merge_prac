import datetime
class File(oshelper):
	"""This requires more support from os for actual working implementation i am just writing a sample"""
	def __init__(self, filename, filetype = ".txt" ,path):
		self.filename = filename
		self.filetype = filetype
		self.path = path
		self.size = getsize(self.path,self.filename) # lets assume os has this method to return the size
		self.createdOn = datetime.datetime.now()
		self.createdBy = getuser.now() 	#lets assume this also gives us the user who created this
