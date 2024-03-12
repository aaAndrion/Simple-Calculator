def calculate():
    operation = input('''
Please type in the operator you want to use:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    try:
        number_1 = float(input('Please enter the first number: '))
        number_2 = float(input('Please enter the second number: '))
    except ValueError as ERROR:
        print("Invalid Number\n")
        print(ERROR)
        print("\nYou did not input a proper number, please try again.")
        return

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print("The total value is:", number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print("The difference of both values is:", number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print("The product of the two values is", number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print("The quotient of the two values is", number_1 / number_2)

    else:
        print('You have entered an invalid operator, please rerun the program again.')

    again()


def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Thank you for using the program, see you again. :)')
        exit(0)

    else:
        again()


while True:
    calculate()
# IT101-1P M3 Final Project - Group 11 - Kalyuleytor Gang
# Members: Rayyan Andi, Mark Raphael Abaya, Alfred Ashley Andrion, Hubert Kevin John Wilbur Bantilan
