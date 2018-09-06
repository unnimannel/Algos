'''Find all permutations of a String - Input String: abc Output: {bca, acb, abc, cba, bac, cab}'''

from itertools import permutations as permutationslib

class PermutationString:
	def __init__(self):
		self.input = "abc"
		pass

	def main(self):
		print('Input : ', self.input)
		print('Output : ', self.caclPermutation(self.input))
		print('Output Using Library : ', self.caclPermutationLib())

	def caclPermutation(self,inputStr):
		permutations = []
		n=len(inputStr)
		if(n == 0):
			permutations.append("")
			return permutations
		first = inputStr[0]
		remaining = inputStr[1:]
		words = self.caclPermutation(remaining)
		for word in words:
			print("\n\n",'word',word)
			wl = len(word)
			print('wl: ',wl)
			for i in range(0,wl+1):
				print('i',i)
				if word:
					prefix=word[0:i]
					suffix=word[i:]
				else:
					prefix=""
					suffix=""
				permutations.append(prefix+first+suffix)
				print('prefix: ',prefix,'suffix: ',suffix,'first: ',first,'remaining: ',remaining,'inputStr: ',inputStr)
				print('permutations',permutations)
		return permutations
		#read https://stackoverflow.com/questions/2565619/algorithm-for-python-itertools-permutations

	def caclPermutationLib(self):
		result=[''.join(x) for x in permutationslib(self.input)]
		return result


obj=PermutationString()
obj.main()