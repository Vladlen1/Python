__author__ = 'vladbirukov'


class myrange:
	def __init__(self, *args):
		length = len(args)
		if length == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1
		elif length == 2:
			self.start = args[0]
			self.stop = args[1]
			self.step = 1
		elif length == 3:
			self.start = args[0]
			self.stop = args[1]
			self.step = args[2]
		else:
			raise TypeError("myrange expected at most 3 arguments, got " + str(length))


	def __iter__(self):
		cur = self.start
		while cur < self.stop:
			yield cur
			cur += self.step


	def __str__(self):
		result = 'myrange(' + str(self.start) + ', ' + str(self.stop)
		if self.step != 1:
			result += ', ' + str(self.step)
		result += ')'
		return(result)


if __name__ == '__main__':
	for i in range(1, 5, 3):
		print(i)

	for i in myrange(1, 5, 3):
		print(i)

	x = [i for i in myrange(10)]
	print(x)

	print(myrange(10))
	print(range(10))