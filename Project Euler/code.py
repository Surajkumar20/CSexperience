""" This code is my attempt to solve all Project Euler problems """

class multiples_3_5:
    """ This class will solve the problem in the link below:
        https://projecteuler.net/problem=1               """
    def func():
        return(sum([i for i in range(1000) if i%3==0 or i%5==0]))

if __name__ == "__main__":
    ap = print(multiples_3_5.func())
