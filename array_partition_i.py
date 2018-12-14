# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.


class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res = 0
        for i in range(0, len(nums)-1, 2):
            res += nums[i]
        return res


s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))

# In this problem, we need to find the max sum of every other integer starting with the initial element. I had a hard time understanding what this problem was asking, so I had to look at a solution to understand what was needed.

# We are given 2n integers so an even amount of integers.

# We need to group these integers into pairs so that the sum of the min of those groups is the largest sum possible

# Since we are grouping in pairs, and we are adding the min of these pairs, you want to group the the smallest possible number, with the next smallest number so that you can have the max possible outcome.

# For example, with the array [1,4,3,2] if you grouped them like [1,4] and [3,2] you are not optimizing for the greatest sum because you with have to add 1 and 2 when you could be adding 1 and 3 if you pair the groups like [1,2] and [3,4]

# By sorting the array, you are optimizing for the largest sum

# You can try and get the max sum but shuffling around the numbers in the example:
# [1,4,3,2] -> min[1,4] + min[3,2] = 3
# [1,4,2,3] -> min[1,4] + min[2,3] = 3
# [1,3,4,2] -> min[1,3] + min[4,2] = 3
# [1,3,2,4] -> min[1,3] + min[2,4] = 3
# [1,2,3,4] -> min[1,2] + min[3,4] = 4
# [1,2,3,4] -> min[1,2] + min[4,3] = 4
# [2,1,3,4] -> min[2,1] + min[3,4] = 4

# Let's try a larger array [7,5,9,6,10,8]
# Now let's try pairing them up and adding the min sum
# [7,5,9,6,10,8] -> min[7,5] + min[9,6] + min[10,8] = 19
# [9,6,5,10,8,7] -> min[9,6] + min[5,10] + min[8,7] = 18
# If we sort this array and then find the sum we have optimized for the larger sum
# [5,6,7,8,9,10] -> min[5,6] + min[7,8] + min[9,10] = 20

# The ideal solution to this problem, is sorting and then adding every other number.
# We can use the sort() method in python to sort
# Then we can iterate over the array. We want to iterate over the length of array - 1 because we don't want to add the last element since that will be largest of the last two elements.
# Within the for loop we can count by 2, so we will add every other element (0+2+4...)
# We can keep adding our element to some result array and once we have added all elements we can return that sum!
