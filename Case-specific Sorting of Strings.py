class Solution:
    def caseSort(self,s):
        #code here
        u_arr = []
        l_arr = [] 
        c_str = []
        for val in s:
            if ord('A') <= ord(val) <= ord('Z'):
                u_arr.append(val)
                c_str.append('U')
            else:
                l_arr.append(val)
                c_str.append('L') 
        
        u_arr.sort()
        l_arr.sort() 
        
        ans = [] 
        i,j = 0,0 
        for val in c_str:
            if val == 'U':
                ans.append(u_arr[j])
                j += 1 
            else:
                ans.append(l_arr[i])
                i += 1 
        
        return ''.join(ans) 
