"""
Program: camper_age_input.py
Author: Jacob Sharpe
Last date modified: 6/03/2020

The purpose of this program is to accept an age number
in years from the user and output the age
in the number of months
"""


def convert_to_months(years):
    months = years * 12
    months = int(months)
    return months


if __name__ == '__main__':
    age_in_years = float(input("Enter the age: "))
    age_in_months = convert_to_months(age_in_years)
    print(str(age_in_years) + ' years is ' + str(age_in_months) + ' months')

# Input       Expected Output         Actual Output
#    5      5 years is 60 months    5.0 years is 60 months
#   5.5     5.5 years is 66 months  5.5 years is 66 months
# 'hello'       error                       error
