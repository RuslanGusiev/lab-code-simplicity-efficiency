"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

'''
L.S. Very good! Potential improvement: use list comprehension. 
'''

X = input("What is the maximal length of the triangle side? Enter a number: ")

max_side = 0

for x in range(5, int(X)):
    for y in range(4, int(X)):
        for z in range(3, int(X)):
            if (x*x == y*y + z*z) and (max_side < x):
                max_side = x
                #print(x, y, z)
                #print(max_side)

print('Max side = ', max_side)

