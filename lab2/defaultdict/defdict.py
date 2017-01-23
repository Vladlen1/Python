__author__ = 'vladbirukov'
class mydefaultdict(dict):
	def __getitem__(self, key):
		try:
			return super(mydefaultdict, self).__getitem__(key)
		except KeyError:
			self[key] = mydefaultdict()
			return self[key]


if __name__ == '__main__':
	x = mydefaultdict()
	x[1][1] = 5
	x[2][1] = 8
	print(x)
	print(x[2])


