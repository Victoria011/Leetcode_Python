# Approach 1: Binary Search
# Runtime Complexity: 
# Space Complexity: 
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # column-wise binary search O(cols * log(rows)) time complexity
        rows, cols = binaryMatrix.dimensions()
        left, right = 0, cols -1
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            seen = any([binaryMatrix.get(r, mid) for r in range(rows)])
            if left == right:
                return -1 if not seen else left        
            if seen:
                right = mid   
            else:
                left = mid + 1

# Approach 2: (faster) Binary Search
# The idea is to perform binary search on every column with constraints:
# 1. Once a value is 1 at col j, search only at col<j
# 2. Since col is initialized at m-1, there is a chance of returning m-1 even if all values are 0. 
# In that case we use flag to keep track of at least 1 solution
# Runtime Complexity: 
# Space Complexity: 
class Solution:
    def binsearch(self, binaryMatrix, x, col): # find leftmost column for row x
        l=0
        r=col
        while(l<r):
            mid = l + (r-l)//2                        
            if(binaryMatrix.get(x,mid)==0):
                l = mid+1
            else:
                r = mid
        if binaryMatrix.get(x,l)==1: # find leftmost
            return l
        else: # not find
            return -1  
        
    def leftMostColumnWithOne(self, binaryMatrix):
        n , m = binaryMatrix.dimensions()        
        min_col=m-1
        flag = False
        for i in range(n):
            if binaryMatrix.get(i,min_col)==1:
                ret = self.binsearch(binaryMatrix,i,min_col)                
                min_col = min(min_col,ret)
                flag = True
        return min_col if flag else -1
        
        