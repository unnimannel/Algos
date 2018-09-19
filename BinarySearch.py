#find an element in a sorted array using Binary Search

class BinarySearch:
	def __init__(self):
		pass
	def main(self):
		inp = [1,23,41,55,67,68,74,85,88,89,92,93,94,99]
		num = 92
		print("Input List: ",inp," Input Number to search: ",num)
		indexx = self.binarysearching(inp,num)
		if indexx >= 0:
			print(num," found at index ",indexx)
		else:
			print(num," not found ")
	def binarysearching(self,inp,num):
		if(len(inp) == 0):
			return -1
		start = 0
		end = len(inp) - 1
		print("End : ",end)
		while start <= end:
			mid = (start + end ) // 2
			if inp[mid] == num:
				return mid
			elif num < inp[mid]:
				end = mid - 1
			else:
				start = mid + 1
		return -1

obj = BinarySearch();
obj.main()