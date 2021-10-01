# Approach 1
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        op=[]
        res=[]
        i=0
        for x,y in points:
            d=x*x+y*y
            res.append([i,d])
            i+=1

        res.sort(key=lambda x:x[1])
        res=res[:k]

        for ind,d in res:
            op.append(points[ind])
        return op

# Runtime Complexity: O(N)
# Space Complexity: O(N)

# Approach 2
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        items = []
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1] 
            items.append((distance, point))
        
        def quickSelect(left, right):
            pivot, p = items[right], left
            for i in range( left, right):
                if items[i][0] < pivot[0]:
                    items[i], items[p] = items[p], items[i] #swap index i and p
                    p += 1
            items[p], items[right] = items[right], items[p] # swap index p and right
            if p == k - 1:
                return
            if p < k - 1:
                quickSelect(p + 1, right)
            else:
                quickSelect(left, p - 1)
        quickSelect(0, len(items) - 1)
        return [items[i][1] for i in range(0, k)]