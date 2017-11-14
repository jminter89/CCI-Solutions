# Given an array arr of unique nonnegative integers, implement a 
# function getDifferentNumber that finds the smallest 
# nonnegative integer that is NOT in the array.
# Even if your programming language of choice doesn’t have 
# that restriction (like Python), assume that the maximum value 
# an integer can have is MAX_INT = 2^31-1. So, for instance, the 
# operation MAX_INT + 1 would be undefined in our case.
# Your algorithm should be efficient, both from a time and a space 
# complexity perspectives.
# Solve first for the case when you’re NOT allowed to modify the input 
# arr. If successful and still have time, see if you can come up with an 
# algorithm with an improved space complexity when modifying arr is allowed. 
# Do so without trading off the time complexity.
# Analyze the time and space complexities of your algorithm.


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def get_different_number(arr):
	arr.sort()
	length = len(arr)

	for i in xrange(length):
		if arr[i] != i:
			return i
	return arr[-1] + 1

# Time Complexity: O(n)
# Space Complexity: O(n)
def get_different_number_hash(arr):
	oracle = {}
	length = len(arr)

	for i in xrange(length):
		oracle[arr[i]] = arr[i]
		
	for i in xrange(2**31-1):
		if oracle.has_key(i) != True:
			return i
    