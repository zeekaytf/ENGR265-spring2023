# # Math Module Here # #

import math
# how well do you know your operators?
# you can add each variable into the print function below
# to check you work, like so:
# print(first_number)

# multiply two factors of 64
first_number = 2*32
print(first_number)
# divide first_number by 10
second_number = first_number/10
print(second_number)
# add second_number to first_number, then subtract 2
third_number = second_number+first_number-2
print(third_number)
# now, using parentheses, divide second_number by 2, then multiply it by 20, and finally add 2.4
fourth_number = (second_number/2)*20 + 2.4
print(fourth_number)
# think of two different ways to raise 8 to the 2nd power
# hint, for one of them you have to import a module discussed in class
squared_number_one = 8**2
print(squared_number_one)
squared_number_two = math.pow(8, 2)
print("The final answer is", squared_number_two)
