#Count frequencies of array elements in range 1 to n

class CountFreqCls:
	def __init__(self):
		self.input = [3,4,4,5,7,4,4]

	def start(self):
		print('input : ',self.input)
		print('count using naive starts')
		self.countFreqNaive()
		print('count using naive ends')
		print('input : ',self.input)
		print('count using normal starts')
		self.countFreq()
		print('count using normal ends')
		print('input : ',self.input)
		print('count using Efficient starts')
		self.countFreqEfficient()
		print('count using Efficient ends')

	def countFreqNaive(self):
		n = len(self.input)
		for i in range(1,n+1):
			count = 0
			for j in range(0,n):
				if self.input[j] == i:
					count += 1
			print(i,' : ',count)

	def countFreq(self):
		n = len(self.input)
		count = {}
		for i in range(1,n+1):
			count[i] = 0
		for i in range(0,n):
			count[self.input[i]] += 1
		print(count)

	def countFreqEfficient(self):
		reducedInput = [x-1 for x in self.input]
		n = len(self.input)
		for i in range(0,n):
			reducedInput[reducedInput[i]%n] = reducedInput[reducedInput[i]%n] + n
		for i in range(0,n):
			print(i+1,' : ',reducedInput[i]//n)
		self.countFreqEfficientGetBackOrig(reducedInput)

	def countFreqEfficientGetBackOrig(self,InputModifiedList):
		n = len(InputModifiedList)
		for i in range(0,n):
			InputModifiedList[i] = InputModifiedList[i]%n + 1
		print(InputModifiedList)
		

obj = CountFreqCls()
obj.start()