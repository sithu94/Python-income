# Function: 1) Income distribution 2) Taxation
# Developer: Si Thu Aung
# Date: 4th January 2017
# Program inputs: Related Incomes 1) Active 2) Passive Incomes
# Input data type: Commandline
# Program outputs: 1) Income distribution chart 2) Taxation Expenses
# Output data type: Visual chart and commandline
###############################################

import matplotlib.pyplot as plt
import scipy
from modules import calculate_tax

# Main Loop
def main():

    # Get the objects
    tx = calculate_tax.Tax
    inter = calculate_tax.Interface

    # Calulate net income
    income = inter.user_income()
    tax = tx.income_tax(income)
    net_income = income - tax

    # get the income distribution
    (mortgage,emergency,managed,side_investment,bills) = tx.income_distribution(net_income)
    income_array = [int(mortgage),int(emergency),int(managed),int(side_investment),int(bills)]

    inter.distribution(income_array)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("The user interrupted the program!")
