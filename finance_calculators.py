import math

print('''\tinvestment - calculate the interest earned on your investment
\tbond - to calculate the amount you'll have to pay on a home loan''')

while True:

    # Choose a finance calculator or exit the program
    menu_choice = input('''
Dear User, take an action!
1. Investment Calculator
2. House Loan Repayment Calculator
3. Exit program
Enter the number next to your desired choice: ''').strip()
    while menu_choice not in ["1", "2", "3"]:
        menu_choice = input('''
\tYOUR INPUT IS INVALID! Try again.
Enter the number next to your desired choice: ''').strip()

    # Acquire the correct amounts for the investment
    if menu_choice == "1":   # investment calculator
        while True:
            try:
                principal_amount = float(input('''
\tENTER NUMERICAL VALUES ONLY.
How much money do you want to deposit? '''))

                interest_rate = float(input('''
As a percentage, what is the interest rate of the investment? '''))

                number_of_years = float(input('''
How many years do you plan on investing? '''))
                break
            except ValueError:
                print('''
....YOUR INPUT IS INVALID! Try again....''')

        # Choose the type of interest rate
        interest = input('''
Dear User, take an action!
1. Simple interest rate
2. Compound interest rate
Enter the number next to your desired choice: ''').strip()

        # Do the calculations (simple interest rate)
        if interest == "1":
            P = principal_amount
            r = interest_rate / 100
            t = number_of_years
            A = P * (1 + r * t)
            print(f'''
After investing R{P:.2f} at a simple interest rate of {interest_rate}(%) for a
period of {t} years, your accumulated amount will be R{A:.2f}''')

        # Do the calculations (compound interest rate)
        else:
            P = principal_amount
            r = interest_rate / 100
            t = number_of_years
            A = P * math.pow((1 + r), t)
            print(f'''
After investing R{P:.2f} at a compound interest rate of {interest_rate}(%) for
a period of {t} years, your accumulated amount will be R{A:.2f}''')

    # Acquire the correct amounts for the home loan repayment
    elif menu_choice == "2":   # home loan repayment calculator
        while True:
            try:
                present_value = float(input('''
\tENTER NUMERICAL VALUES ONLY.
What is the present value of the house? '''))

                interest_rate = float(input('''
As a percentage, what is the monthly interest rate of the bond repayment? '''))

                number_of_months = float(input('''
How many months do you plan to take in order to repay your bond? '''))
                break
            except ValueError:
                print('''
....YOUR INPUT IS INVALID! Try again....''')

        # Do the calculations (home loan interest)
        P = present_value
        i = (interest_rate / 12) / 100
        n = number_of_months
        repayment = (i * P) / (1 - (1 + i) ** (-n))
        print(f'''
While the house is still worth R{P:.2f}, you will have to
repay R{repayment:.2f} each month at a monthly interest rate of
{interest_rate}(%) for a period of {n} months.''')

    # Exit the program
    elif menu_choice == "3":
        print("\n\tGoodbye, user.")
        exit()
