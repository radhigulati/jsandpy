class Solution:
    def sortArrayByParity(self, A):
        # find all even elements and append them to new array then find all odd elements and append them to new array
    
        E = []
        O = []
        for i in A:
            if i % 2 == 0:
                E.append(i)
            else:
                O.append(i)
        return E+O

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))
