"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

try:
    a = input('Please choose your first number (zero to five): ')
    b = input('What do you want to do? plus or minus: ')
    c = input('Please choose your second number (zero to five): ')
except ValueError:
    print("I am not able to answer this question. Check your input.")

# funcrtion 'converting' string to number with values for 'a' and 'c'
def string_to_number(x):
    if x == 'zero':
        x = 0
    elif x =='one':
        x = 1
    elif x =='two':
        x = 2
    elif x =='three':
        x = 3
    elif x =='four':
        x = 4
    elif x =='five':
        x = 5
    return x

# funcrtion 'converting' number to string. - for output result in string
def number_to_string(x):
    if x == 0:
        x = 'zero'
    if x == 1:
        x = 'one'
    if x == 2:
        x = 'two'
    if x == 3:
        x = 'three'
    if x == 4:
        x = 'four'
    if x == 5:
        x = 'five'
    if x == 6:
        x = 'six'
    if x == 7:
        x = 'seven'
    if x == 8:
        x = 'eigth'
    if x == 9:
        x = 'nine'
    if x == 10:
        x = 'ten'
    return x

# function calculator, 'a' and 'c' values that we subtract or plus - 'b'
def result(a, b, c):
    if b == 'plus':
        x = string_to_number(a) + string_to_number(c)
        print(a +' '+b+' ' + c, 'equals', number_to_string(x))
    elif (b == 'minus') and (string_to_number(a) >= string_to_number(c)):
        x = string_to_number(a) - string_to_number(c)
        print(a +' '+b+' ' + c, 'equals', number_to_string(x))
    elif (b == 'minus') and (string_to_number(a) < string_to_number(c)):
        x = string_to_number(c) - string_to_number(a)
        print(a +' '+b+' ' + c, 'equals negative', number_to_string(x))

result(a, b, c)
