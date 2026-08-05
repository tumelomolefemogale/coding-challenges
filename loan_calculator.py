'''Given a loan amount, annual interest rate percentage, and fixed monthly payment, return an array of remaining balances after each monthly payment until the loan is paid off.
Each month, interest is calculated on the remaining balance using the monthly interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
Return each remaining balance rounded to the nearest dollar.
Include the loan amount in the returned array. The first element in the array will always be the loan amount, and the last element of the array will always be 0.'''


def get_loan_schedule(loan_amount, annual_interest_percentage, fixed_monthly_payment):
    array = [loan_amount]

    while array[-1] > 0:
        interest = array[-1] * ((annual_interest_percentage / 100) / 12)
        new_amount_owed = (array[-1] + interest) - fixed_monthly_payment
        if new_amount_owed >= 0:
            array.append(round(new_amount_owed))
        else:
            array.append(0)

    return array


print(get_loan_schedule(1000, 0, 200))
print(get_loan_schedule(1000, 5, 200))
print(get_loan_schedule(10, 50, 1))
print(get_loan_schedule(5500, 8, 400))
print(get_loan_schedule(50000, 5.2, 1650))
