# Question 1

first_number = int(input("Enter the first number: "))

second_number = int(input("Enter the second number: "))

total_sum = first_number + second_number

print(f"The sum of {first_number} and {second_number} is {total_sum}.")

# Question 2

favorite_animal = input("What's your favorite animal? ")

print(f"My favorite animal is also {favorite_animal}!")

# Question 3
temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Converting temperature into Celsius:
temperature_celsius = (temperature_fahrenheit - 32) * 5.0 / 9.0

print(f"Temperature: {temperature_fahrenheit}F = {temperature_celsius}C")

# Question 4

side1 = float(input("What is the length of side 1? "))
side2 = float(input("What is the length of side 2? "))
side3 = float(input("What is the length of side 3? "))

perimeter = side1 + side2 + side3

print(f"The perimeter of the triangle is {perimeter}")

# Question 5

number = int(input("Type a number to see its square: "))

square = number * number

print(f"The Square of {number} is {square}")

# Question 6

numbers = [1, 2, 3, 4, 5]

numbers.remove(3)

print(f"Updated list after removing 3: {numbers}")

# Question 7

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(f"Updated list1 after adding elements of list2: {list1}")

# Question 8

items = [10, 20, 30, 40]

popped_value = items.pop()

print(f"Updated items list after pop: {items}")
print(f"Value removed: {popped_value}")

# Question 9

colors = ['red', 'blue', 'green', 'yellow']

index_of_green = colors.index('green')

print(f"The index of 'green' in the colors list is: {index_of_green}")

# Question 10

def get_last_element(lst):
    print(lst[-1])

list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
get_last_element(list)  

# Question 11

def get_user_list():
    user_list = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)
    print(f"Here's the list: {user_list}")

get_user_list()


