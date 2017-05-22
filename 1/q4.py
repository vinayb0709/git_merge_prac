class Qsn():
	"""docstring for Qsn"""
	def __init__(self, qsn, ans):
		self.qsn = qsn
		self.ans = ans
	def eval(self,attempt):
		self.marks = 0;
		if attempt == self.ans:
			self.marks = 3;
			return "Right"
		else:
			self.marks = -1;
			return "Wrong"
	def correctAns(self):
		return self.ans
	def Marks(self):
		return self.marks

x = Qsn("2+2?","4")
print x.eval("3")
print x.correctAns()
print x.Marks()