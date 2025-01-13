class Solution:
    def maxWater(self, arr):
        # code here
        left , right = 0,len(arr)-1
        mx_area = 0
        while left <= right:
            val1,val2 = arr[left],arr[right]
            area = min(val1,val2)*(right-left)
            mx_area = max(area,mx_area)
            
            if val1 >= val2:
                right -= 1
            else:
                left += 1 
        
        
        return mx_area
        
