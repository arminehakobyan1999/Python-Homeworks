import Productcheck

def buy(product, num, price):
    if Productcheck.check(product, num):
        return print("You bought {} and spent {}".format(product, num*price))
    else:
        return print("Sorry! We are out of this product.")

