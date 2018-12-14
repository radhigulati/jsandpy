# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.


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
print(s.sortArrayByParity([3, 1, 2, 4]))

# In this problem, we want to arrange the array so that the even elements come first and the odd elements follow.

# To do this, I created two new empty arrays - one for my even elements and one for my odd elements

# I then have a for loop that iterates through the array and checks to see if an elements is even (i%2==0) and if it is even, I push that element into the even array (E)

# If the element is not even, the element is pushed into the odd array (O)

# Once the for loop is done executing, I concat the arrays together with the '+' operator and return that as the result
