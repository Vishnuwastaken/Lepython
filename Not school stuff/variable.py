# program to display msgs
# name = 'Vishnu'
# age = 15
# marks = 5.9
# print(name, 'is', age, 'years old', 'and his marks are', marks)

# program to find area
# length = int(input('Enter the length: '))
# width = int(input('Enter the width: '))
# area = length*width
# print(f'The area is {area}')

# program to input time in minutes and display in hours and minutes
# time = int(input('What is your time: '))
# hours = time//60
# minute = time%60
# print(hours, 'hours', 'and', minute, 'minutes')

# write program to input marks of student in 3 subject out of 100
# eng = int(input('Enter your english grades: '))
# comp = int(input('Enter your computer science grades: '))
# math = int(input('Enter your math grades: '))
# avg = (math+comp+eng)/3
# print(f'Your average is {avg}')

# write program to input two-digit number and show the sum of the digits of the number (show next class)
x = int(input('Enter a 2 digit number:  '))
if 100 > x > 10:
    first_number = x // 10
    last_number = x % 10
    add = first_number + last_number
    print(f'\nThe first digit is {first_number}\nThe second digit is {last_number}')
    print(f'The sum of both numbers are {add}')
else:
    print('That is not 2 digit number')

