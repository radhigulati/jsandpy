# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]


class Solution(object):
    def flipAndInvertImage(self, A):
        for a in xrange(0, len(A)):
            # flip horizontally
            A[a] = A[a][::1]
            # invert image
            A[a] = [1 if i == 0 else 0 for i in A[a]]
        return A


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))

# OVERVIEW

# This questions asks us to take a matrix and flip the image horizontally and then invert it
# When we flip an image horizontally, that means we are reversing the array.
# For example: [0,1,1] -> [1,1,0]
# After we flip the image horizontally, we need to invert it
# This is done by replacing a 1 with a 0 and vice versa
# For example: [0,1,1] -> [1,0,0]
# Here is an example if we want to flip and image horizontally and invert it:
# [1,0,0] -> [0,0,1] -> [1,1,0]
# Great! Now we need to do that for all of the rows within the matrix
# I first iterate through the matrix using a for loop. You need to use len(A) so that we are iterating over integers
# Once we enter the for loop, we can begin reversing each row.
# To do this, we can use a nice python slice trick
# In python, [::-1] can be used to reverse an array
# For example: [0,1,1][::1] -> [1,1,0]
# We are using 'a' to point at the index so if we begin our for loop A[a] would be A[0] which would be our first row of [1,1,0]
# If we set A[a] = A[a][::-1] we can reverse our row
# To invert the row, we can iterate through our row and everytime we see a 0 we can set it to 1 otherwise set the number to 1
# Here we can use a nice one liner that sets A[a] = (1 if i == 0 else 1 for i in A[a])
# Once the for loop is done executing we can return A
