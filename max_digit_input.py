
#This program allows a user to input natural numbers then gets the largest in the list.

my_list = []

print("Please input the numbers and 'exit' to break out of the loop")

while True:
    user_input = input()

    if user_input.lower() == 'exit':
        break

    my_list.append(user_input)

    largest_digit = my_list[0]
    for x in my_list:
         if x > largest_digit:
             largest_digit = x

print(f"The largest digit in the list is {largest_digit}")