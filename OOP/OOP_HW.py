# Make a class called Restaurant
class Restaurant:

    def __init__(self, n, c):
        self.name = n
        self.cuisine = c

    def open_restaurant(self):
        print(f'{self.name}  is open')

    def describe_restaurant(self):
        print('---------')
        print(f'The restaurant is called {self.name} ')
        print(f'The restaurant has {self.cuisine} food')
        print('---------')


restaurant = Restaurant('Fast Food Heaven', 'American')
print(restaurant.name, restaurant.cuisine)
restaurant.open_restaurant()
restaurant.describe_restaurant()

R2 = Restaurant('Oui Oui Baguette', 'French')
R2.describe_restaurant()

R3 = Restaurant('Indian Dhaba', "Indian")
R3.describe_restaurant()

R4 = Restaurant('Spagett', 'Italian')
R4.describe_restaurant()


# class called user
class User:

    def __init__(self, fn, ln, age, nation):
        self.first_name = fn
        self.last_name = ln
        self.age = age
        self.nationality = nation

    def describe_user(self):
        print('---------')
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Nationality: {self.nationality}')
        print()

    def greet_user(self):
        print(f'Hi {self.first_name} hope you are well :D')
        print('---------')


User1 = User('Bob', 'Smith', 18, 'American')
User1.describe_user()
User1.greet_user()

User2 = User('Kai', 'Hiroshi', 85, 'Japanese')
User2.describe_user()
User2.greet_user()

User3 = User('Shreyas', 'Ayyengar', 15, 'British/Indian')
User3.describe_user()
User3.greet_user()

User4 = User('Jason', 'Jacob', 39, 'Greece')
User4.describe_user()
User4.greet_user()

User5 = User('Mohammed', 'Khan', 56, 'Kuwait')
User5.describe_user()
User5.greet_user()
