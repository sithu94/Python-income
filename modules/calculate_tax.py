# Function: Calculate Taxation
# Developer: Si Thu Aung
# Date: 4th January, 2017
# Program inputs: 1) Active income 2) Passive Income
# Input data type: Numeric
# Program outputs: Total Income
# Output data type: Numeric and Visual
##########################################################

import matplotlib.pyplot as plt
import scipy

class Tax:
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