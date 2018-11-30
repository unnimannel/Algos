# Given a dictionary of words and a string of characters, find if the string of characters can be broken into individual valid words from the dictionary.
# Example: 
# Dictionary: arrays, dynamic, heaps, IDeserve, learn, learning, linked, list, platform, programming, stacks, trees
# String    : IDeservelearningplatform
# Output   : true 

class WordBreakProblem:
	def __init__(self):
		self.dictionaryy = {"arrays": True, "dynamic": True, "heaps": True, "IDeserve": True, "learn": True, "learning": True, "linked": True, "list": True, "platform": True, "programming": True, "stacks": True, "trees": True}
	def main(self):
		if(self.hasValidWords('programminglearn')):
			print('true')
		else:
			print('false')
	def hasValidWords(self,inp_str):
		if inp_str is None or len(inp_str) == 0:
			return True
		lengt = len(inp_str)
		valid_words = [False]*lengt
		for i in range(0,lengt):
			if self.dictionaryy.get(inp_str[0:i+1]):
				valid_words[i] = True
			if valid_words[i] == True and i == lengt-1:
				return True
			if valid_words[i] == True:
				for j in range(i+1,lengt):
					if self.dictionaryy.get(inp_str[i+1:j+1]):
						valid_words[j] = True
					if j == lengt-1 and valid_words[j] == True:
						return True
		return False

obj = WordBreakProblem()
obj.main()