# Program that asks the user for a number and prints all the even numbers from 1 to that number using a for loop.

number = input('Enter a number: ')
num = int(number)

for num in range(1, num):
    if (num % 2) == 0:
        print(num)