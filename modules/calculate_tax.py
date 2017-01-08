# Function: Calculate Taxation
# Developer: Si Thu Aung
# Date: 4th January, 2017
# Program inputs: 1) Active income 2) Passive Income
# Input data type: Numeric
# Program outputs: Total Income
# Output data type: Numeric and Visual
##########################################################

import matplotlib.pyplot as plt

class Tax:
    # Calculate income tax depending on the income
    def income_tax(income):
        if income <= 18200:
            active_tax = 0
        elif (income>18200) & (income<=37000):
            active_tax = 0.19*(income-18200)
        elif (income>37000) & (income<=80000):
            active_tax = 3572+(0.325*(income-37000))
        elif (income>80000) & (income<=180000):
            active_tax = 17547+(0.37*(income-80000))
        elif (income>180000):
            active_tax = 54547+(0.45*(income-180000))

        return active_tax

    # Create the income distribution
    def income_distribution(net_income):
        mortgage = 0.15*net_income
        emergency = 0.2*net_income
        managed = 0.2*net_income
        side_investment = 0.2*net_income
        bills = 0.15*net_income

        return (mortgage,emergency,managed,side_investment,bills)

class Interface:
    # Request User Income Data
    def user_income():
        active = input("Type your active income in AUD: ")
        var = input("Do you have any passive income (y/n)?: ")

        if var == "y":
            passive = input("Type your passive income in AUD: ")
        elif var == "n":
            passive = 0

        return (int(active)+int(passive))

    # Display User Income distribution
    def distribution(income_array):

        """Input array contains 5 components of the portfolio
           1st = mortgage, 2nd = emergency, 3rd = managed, 4th = side_investment,
           5th = billls """

        # Data to plot
        labels = "Mortgage","Emergency","Managed Funds","Side Investment","Bills"
        sizes = [income_array[0],income_array[1],income_array[2],income_array[3],income_array[4]]
        colors = ['yellow','red','blue','gold','green']
        explode = (0.1,0,0.2,0.2,0.1)

        # Plot
        plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()
