# This program selects the largest number and prints on the standard output

my_numbers = [2,6,7,9,9,8,1,0]

largest_digit = my_numbers[0]

for number in my_numbers:
    if number > largest_digit:
        largest_digit = number

print(f"The largest number in the list is {largest_digit}") 

