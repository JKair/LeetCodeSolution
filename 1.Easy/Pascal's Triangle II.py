class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        for i in xrange(rowIndex+1):
        	for j in xrange(i,-1,-1):
        		if j == 0:
        			break
        		if j == i:
        			result.append(1)
        		else:
        			result[j] = result[j] + result[j-1]
        return result