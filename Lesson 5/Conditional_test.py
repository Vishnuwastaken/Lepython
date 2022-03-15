separator = "**** ~ *** ~ ****"
print(separator)
print("Welcome to my App")
print(separator)

exitApp = False
while not exitApp:
    percentage = int(input("Enter your percentage (0 to 100): "))
    # test = percentage > 50
    # print(test)

    if percentage >= 90 and percentage <= 100:
        print("That's a 7!")
    elif percentage >= 80 and percentage <= 89:
        print("That's a 6!")
    # *** add other conditions ***
    # elif percentage < 0:
    #     exitApp = True
    #     print("Goodbye!")
    else:
        print("Invalid input. Please try again.")

    ans = input("Try again? (Y/N) ")
    if ans.upper() == 'N':
        exitApp = True

print("Goodbye. Cya later 👋.")
print(separator)