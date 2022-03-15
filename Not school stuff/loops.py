# write a program to input a 3-digit number
# digit = int(input('Enter a 3 digit number: '))
# while not (100 <= digit < 1000):
#     print('This is not a 3 digit number!!')
#     digit = int(input('Enter a 3 digit number now!: '))
# print('Thank you for finally entering a 3 digit number!')

# write a program to input a character until the user enters a alphabet
# character = input('Enter a character: ')
# while not ('a' <= character.lower() <= 'z'):
#     print('This is not an alphabet. Something else idk.')
#     character = input('Enter an alphabet: ')
# print('Finally you entered a alphabet')

# write a calculator program that runs until the user exits
# username = input('Enter your name: ')
# print(f'Welcome {username} to my calculator!')
# print('There are 4 different operations you can do, 1. Add, 2. Subtract, 3. Multiply, 4. Divide, or 5 to exit')
# while True:
#     number = float(input('Enter your first number: '))
#     number1 = float(input('Enter your second number: '))
#     print('1. Add')
#     print('2. Subtract')
#     print('3. Multiply')
#     print('4. Divide')
#     print('5. Exit')
#     choice = input('What would you like to do?: ')
#     if choice == '1' or choice.lower() == 'add':
#         print(number + number1)
#
#     elif choice == '2' or choice.lower() == 'subtract':
#         print(number - number1)
#
#     elif choice == '3' or choice.lower() == 'multiply':
#         print(number * number1)
#
#     elif choice == '4' or choice.lower() == 'divide':
#         print(number / number1)
#
#     elif choice == '5' or choice.lower() == 'exit':
#         print(f'Goodbye {username}, You will be missed')
#         break
#     else:
#         print(f'That is not a valid option {username}, you idiot')

# enter someone's name and age. If they are a teenager welcome them, and don't let them continue if not teen.
# name = input('Enter your name: ')
# age = int(input(f'Hey {name.title()}, please enter your age: '))
# while not (13 <= age <= 19):
#     print(f'{name.title()}, You are not a teenager!!')
#     age = int(input(f'Enter till you are teenager, {name.title()}!: '))
# print(f'Welcome to being a teenager, {name.title()}!')

# write a program to input salary of employees and display the highest salary
# max = 0
# while True:
#     salary = int(input('Enter your salary: '))
#     if salary > max:
#         max = salary
#     again = input('Type Y or Yes to continue and any other key to exit: ')
#     if again != 'Yes'.lower() and again != 'Y'.lower():
#         print('Goodbye.')
#         break
# print(f'Your highest salary was {max} $')

# write a program to input the name and salary of employees and display the name of the person with highest salary
# max = 0
# richguy = ""
# while True:
#     name = input(" Enter the employee's name: ")
#     salary = int(input(f"Enter {name.title()}'s salary: "))
#     if salary > max:
#         max = salary
#         richguy = name
#     again = input('Type Y or Yes to continue and any other key to exit: ')
#     if again != 'Yes'.lower() and again != 'Y'.lower():
#         print('Goodbye.')
#         break
# print(f'{richguy} has the highest salary of {max}$')

# add minimum wage to code above ^^^
# max = 0
# min = 10000
# richguy = ""
# poorguy = ""
# while True:
#     name = input(" Enter the employee's name: ")
#     salary = int(input(f"Enter {name.title()}'s salary: "))
#     if salary <= min:
#         min = salary
#         poorguy = name
#     if salary > max:
#         max = salary
#         richguy = name
#     again = input('Type Y or Yes to continue and any other key to exit: ')
#     if again != 'Yes'.lower() and again != 'Y'.lower():
#         print('Goodbye.')
#         break
# print(f'{richguy.title()} has the highest salary of {max}$')
# print(f'{poorguy.title()} has the lowest salary of {min}$')

# enter the age of students and count how many students are not yet teenagers
# count = 0
# while True:
#     age = int(input('Enter your age: '))
#     if age < 13:
#         count += 1
#     again = input('Type Y or Yes to continue and any other key to exit: ')
#     if again != 'Yes'.lower() and again != 'Y'.lower():
#         print('Goodbye.')
#         break
# print(f'There are {count} people who are not teens.')

# Write a program to count 3 categories of ppl, Children (Less than 18), Adults (18-59),Seniors(60+)
# minor = 0
# adult = 0
# senior = 0
# while True:
#     age = int(input('Enter your age: '))
#     if age < 18:
#         minor += 1
#         again = input('(Y/Yes) to continue or (Any other key) to exit: ')
#         if again != 'Yes'.lower() and again != 'Y'.lower():
#             print('Goodbye.')
#             break
#     if 18 <= age <= 59:
#         adult += 1
#         again = input('(Y/Yes) to continue or (Any other key) to exit: ')
#         if again != 'Yes'.lower() and again != 'Y'.lower():
#             print('Goodbye.')
#             break
#     if age >= 60:
#         senior += 1
#         again = input('(Y/Yes) to continue or (Any other key) to exit: ')
#         if again != 'Yes'.lower() and again != 'Y'.lower():
#             print('Goodbye.')
#             break
# print(f'There is {minor} Children!')
# print(f'There are {adult} Adults!')
# print(f'There are {senior} Senior citizens!')
