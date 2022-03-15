# define a class pony that has a name, color, and age
# class Pony:
#     def __init__(self, name, color, ag):
#         self.name = name
#         self.color = color
#         self.age = ag
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, new_age):
#         self.age = new_age
#
#
# nm = input('Enter a name for your unicorn: ')
# clr = input('Enter a color for your unicorn: ')
# age = int(input("Enter the unicorn's age: "))
# P1 = Pony(nm, clr, age)
# print(f'The name of ur pony is: {P1.get_name().title()}')
# new_name = input('Enter a new name for your pony: ')
# P1.set_name(new_name)
# print(f'The new name of your pony is {P1.get_name().title()}')
# P1.set_age(age+1)
# print(f'The age of ur pony is {P1.get_age()}')

# def a class
# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2*self.length + 2*self.width
#
# rec = Rectangle(10,5)
# print(f'The area is {rec.area()}')
# print(f'The perimiter is {rec.perimeter()}')

L = []
while True:
    color = input("Enter a color: ")
    L.append(color)
    choice = input('DO you wanna continue? Type (Y or Yes) to continue and any other key to exit: ')
    if choice.lower() != 'y' and choice.lower() != 'yes':
        break
number = int(input('Enter the position of color: '))
print(L[number-1])
print(f'Your colors are {L} ')
