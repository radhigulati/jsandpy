# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

# You may return any answer array that satisfies this condition.


class Solution:
    def sortArrayByParityII(self, A):
        res = A
        even = [num for num in A if num % 2 == 0]
        odd = [num for num in A if num % 2 == 1]
        res[::2] = even
        res[1::2] = odd
        return res


s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))

# For this problem, we want to make sure each even index is associated with an even elements and each odd index is associated with an odd index
# To do this, we can create a 'result' variable that is equal to the array that is given through the input
# Then we can create two variables called even and odd
# The even variable will contain all of the even elements from A and the odd variable will contain all the odd elements from A
# To do this, we iterate over A with a one liner for each variable
# Next, to make sure each index is associated with the correct elements, we will splice the result array
# When we slice res[::2] we are saying all of the even spots in result starting from index 0 will be taken by even elements.
# When we slice res[1::2] we are saying starting from index 1 and every other element will be taken by odd elements
# We can then return our res array which will contain the correct array
