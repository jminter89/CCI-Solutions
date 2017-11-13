# The deletion distance of two strings is the minimum 
# number of characters you need to delete in the two strings 
# in order to get the same string. For instance, the deletion 
# distance between "heat" and "hit" is 3:
# 
# By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get 
# the string "ht" in both cases. We cannot get the same string 
# from both strings by deleting 2 letters or fewer. Given the 
# strings str1 and str2, write an efficient function 
# deletionDistance that returns the deletion distance between 
# them. Explain how your function works, and analyze its time and 
# space complexities.

# Time Complexity O(2^n)
# Space Complexity O(2^n)
def deletion_distance_recurse(str1, str2):
  if str1 == "":
    return len(str2)
  if str2 == "":
    return len(str1)
  if str1[0] == str2[0]:
    return deletion_distance(str1[1:], str2[1:])
  dd1 = deletion_distance(str1[1:], str2) + 1
  dd2 = deletion_distance(str1, str2[1:]) + 1
  return min(dd1, dd2)

# Time Complexity O(n)
# Space Complexity O(n)
def deletion_distance_loop(str1, str2):
	len1 = len(str1) + 1
	len2 = len(str2) + 1

	dp = [[0]*(len1) for _ in xrange(len2)]
	for i in xrange(1,len1):
		dp[0][i] = i
	for i in xrange(1,len2):
		dp[i][0] = i
	for i in xrange(1, len1):
		for j in xrange(1, len2):
			if str1[i-1] == str2[j-1]:
				dp[j][i] = dp[j-1][i-1]
			else:
				dp[j][i] = min(dp[j-1][i], dp[j][i-1]) + 1
	return dp[-1][-1]


  if __name__=="__main__":