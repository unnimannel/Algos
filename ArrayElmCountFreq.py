#Count frequencies of array elements in range 1 to n

class CountFreq:
	def __init__(self):
		self.input = [3,4,4,5,7,4,4]

	def start(self):
		self.countFreqNaive()

	def countFreqNaive(self):
		n = len(self.input)
		for i in range(1,n+1):
			count = 0
			for j in range(0,n):
				if self.input[j] == i:
					count += 1
			print(i,' : ',count)
		

obj = CountFreq()
obj.start()