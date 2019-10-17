"""
The code below generates a given number of random strings that consists of numbers and
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

'''
L.S. Very good! Nice and succint code. Minor improvements: (1) use range and ascii module to get the words and chars; 
(2) if min_length > max_lenght I get an error. 
'''

import random

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

total_list = []

min_len = input('Enter minimum string length: ')
max_len = input('Enter maximum string length: ')
words_number = input('How many random strings to generate? ')

for i in range(int(words_number)): # number of words in total list
    word = ''
    rand = random.choice(range(int(min_len), int(max_len))) # number of letters in future word
    for j in range(rand): # create a word
        word += random.choice(a) # get random letter from list 'a'
    total_list.append(word) # add new word to total list

print(total_list)