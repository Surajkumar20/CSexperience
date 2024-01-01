import numpy as np
from matplotlib import pyplot as plt
from forex_python.converter import CurrencyRates

# Internal units will be on a monthly basis and work in USD only
class Suraj:
    def __init__(self, takehomeMoney_MYR_month, takehomeMoney_USA_biweekly):
        self.currency = CurrencyRates()
        self.purdueMoneySpentpYear = 56000
        self.MYR_income_month  = self.currency.convert("MYR", "USD", takehomeMoney_MYR_month)
        self.MYR_expense_month = self.currency.convert("MYR", "USD", 1500) # Assume that I spend RM 1500 per month
        self.USD_income_month  = 2 * takehomeMoney_USA_biweekly
        self.USD_expense_month = 600
        self.currentMoney = 60000 # USD

    # How many months to pay off college tuition in USA
    def targetTime_USA(self):
        time = (self.purdueMoneySpentpYear * 4 - self.currentMoney) / (12*(self.USD_income_month - self.USD_expense_month))
        return 12*time

    # How many months to pay off college tution in MYR
    def targetTime_MYR(self):
        time = (self.purdueMoneySpentpYear*4 - self.currentMoney) / (12*(self.MYR_income_month - self.MYR_expense_month))
        return 12*time

    # how many 
    def yrlyPay(self, country):

        if country == "MYR":
            return 12*self.takehomeMoney_MYR_month
        
        if (country == "USA"):
            return 26*self.takehomeMoney_USA_biweekly
        
        return -1

    # Duration in yrs
    def moneyMade_duration(self, duration, country):
        if country == "MYR":
            return duration * 26 * self.takehomeMoney_MYR_month
        
        elif country == "USA":
            return duration * 26 * self.takehomeMoney_USA_biweekly
        
        else:
            return -1

def payofftime():
    start = 206775
    monthly = 6000
    expenditure = 2000
    print("The number of months required to payoff is {:1f} yrs".format(    (start / (monthly - expenditure))/12  ))
    return

if __name__ == "__main__":
    print("The money you get into Chase is {:.2f}".format(cool(1524.70)))
    payofftime()