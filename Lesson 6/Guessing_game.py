import random
# print(random.randint(0, 9))

separator = "****** ~ **** ~ **** ~ ******"
print(separator)
print("Welcome to my Guessing Game!")
print(separator)

name = input("Please enter your name: ")
begin = input(f"Hello, {name}. Are you ready to start? (Y/N): ")

if begin.upper() == "Y":
    # play the game
    point = 0
    exitApp = False
    start = 0
    end = 9
    ranNum = random.randint(start, end)
    while not exitApp:
        # ranNum = random.randint(start, end)
        # print(ranNum)   # for debugging
        ans = int(input(f"Enter a number from {start} to {end}: "))

        if ans == ranNum:
            point = point + 1
            print(f"Congrats! Now you have {point} point(s)!")
            ranNum = random.randint(start, end)
        else:
            print("Incorrect.")

        again = input("Try again? (Y/N): ")
        if again.upper() == "N":
            exitApp = True

    print(f"Your total points are: {point}")

print(f"Goodbye {name.title()}, See you later")
print(separator)
