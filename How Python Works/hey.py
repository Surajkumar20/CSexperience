import finance as fin

def test1():
    newTakeHome = 1524.70
    malaysiaTakeHome_month = 3000
    objectPlease = fin.Suraj(malaysiaTakeHome_month, newTakeHome)
    print(objectPlease.yrlyPay("MYR"))
    
    # N

def test2():
    takehomeMoney_Malaysia_month = 10000 # in RM
    takehomeMoney_USA_biweekly = 1539#1450# 2268 #1524.70 # paycheck amount per month

    myClass = fin.Suraj(takehomeMoney_Malaysia_month, takehomeMoney_USA_biweekly)
    print("If I take back RM3000 per month, it will take {} months to pay off tuition fees".format(myClass.targetTime_MYR()))
    print("If I take back $50000 per year, it will take {} months to pay off tuition fees".format(myClass.targetTime_USA()))

    # Opportunity cost of the money I let per year
    USA_3_yr_45000 = 3 * 12 * (myClass.USD_income_month - myClass.USD_expense_month)
    USA_3_yr_75000 = 3 * 12 * (2268*2 - 600)
    print("The money that I lose across 3 years if I reduce my own salary from $75000 to ${}: {}.".format(45000, USA_3_yr_75000 - USA_3_yr_45000))
    print("How much I will make per year @ $50000/yr: {}".format(USA_3_yr_45000 / 3))
    
if __name__ == "__main__":
    test2()