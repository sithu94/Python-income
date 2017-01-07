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
    # Request User Income Data
    active = input("Type your active income in AUD: ")
    var = input("Do you have any passive income (y/n)?: ")

    if var == "y":
        passive = input("Type your passive income in AUD: ")
    elif var == "n":
        passive = 0

    tx = calculate_tax.Tax




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("The user interrupted the program!")
