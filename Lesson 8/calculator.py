def sun(num1, num2):
    ans = num1 + num2
    return ans


def mul(num1, num2):
    ans = num1 * num2
    return ans


def sub(num1, num2):
    ans = num1 + num2
    return ans


def div(num1, num2):
    ans = num1/num2
    return ans


def print_ans(ans):
    print(f'The answer is: ' + str(ans))


print('Welcome to my Calculator program.')
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opt = input("What would you like to do? Enter +, -, / or * : ")

if opt == '+':
    print_ans(sun(num1, num2))

if opt == '*':
    print_ans(mul(num1, num2))

if opt == '-':
    print_ans(sub(num1, num2))

if opt == '/':
    print_ans(div(num1, num2))
