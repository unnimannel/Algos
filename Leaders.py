''' Given an array of integers, print the leaders in the array. A leader is an element which is larger than all the elements in the array to its right.
For example:
Input Array:
{ 98, 23, 54, 12, 20, 7, 27 }
Output:
Leaders- 27 54 98 '''

class leaders:
	def __init__(self):
		pass
	def main(self,inputList):
		print("Input List : ",inputList)
		n=len(inputList)-1
		print("Leaders : ")
		leader = inputList[n]
		print(leader)
		while n>=0:
			n-=1
			if inputList[n] > leader:
				leader = inputList[n]
				print(leader)

obj=leaders()
obj.main([78,34,55,41,36,77,44,6,56,7])