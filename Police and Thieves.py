import heapq

class Solution:
    def catchThieves(self, arr, k):
        police = []
        thief = []
        
        for i in range(len(arr)):
            if arr[i] == 'T':
                heapq.heappush(thief, i)
            elif arr[i] == 'P':
                heapq.heappush(police, i)
        
        counter = 0
        
        while police and thief:
            if abs(police[0] - thief[0]) <= k:
                counter += 1
                heapq.heappop(police)
                heapq.heappop(thief)
            elif police[0] < thief[0]:
                heapq.heappop(police)
            else:
                heapq.heappop(thief)
        
        return counter

