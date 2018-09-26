''' Find a Peak Element in an array
Given an array of size n, find a peak element in the array. Peak element is the element which is greater than or equal to its neighbors.
For example - In Array {1,4,3,6,7,5}, 4 and 7 are peak elements. We need to return any one peak element. '''

class peak:
	def __init__(self):
		pass
	def main(self,inp):
		print('Input List : ',inp)
		peakindex = self.peakcalc(inp)
		if peakindex >= 0:
			print('Peak Element : ',inp[peakindex])
		else:
			print('No Peak Element found')
	def peakcalc(self,inp):
		start = 0
		end = len(inp) - 1
		length = len(inp) - 1
		while start <= end:
			mid = (start+end)//2
			if (mid == 0 or inp[mid - 1] <= inp[mid]) and (mid == length):
				return mid
			elif (mid == 0 or inp[mid - 1] <= inp[mid]) and (inp[mid] >= inp[mid+1]):
				return mid
			elif mid > 0 and inp[mid - 1] > inp[mid]:
				end = mid - 1
			else:
				start = mid + 1
		return -1

obj = peak()
obj.main([15, 20, 25, 35, 45, 50, 60])