def menu():
    print("what type of drink would you like?")
    print("1)brewed coffee")
    print("2)latte")
    choice = eval(input("Enter your choice(1-2): "))
    return choice

def brewedPrice(size):
    if size == "small":
        price = 1.60
    elif size == "medium":
        price =1.80
    else: 
        price =2.00
    return price

def lattePrice(size):
    if size == "small":
        price = 2.80
    elif size == "medium":
        price = 3.20
    else:
        price = 3.60

    syrup = input("Flavored syrup (yes or no)")
    if syrup == "yes":
        price += 0.50
    return price


def computetax(price):
    student = input("Are you a student (yes or no)")
    if student == "no":
       tax = price * 0.0625
    else:
        tax =0.0
    return tax


def printResults(price,tax):
    print("--------------------------------------")
    print(" base price : " + format(price, ".2f"))
    print(" tax        : " + format(tax, ".2f"))
    print(" total price: " + format(price, ".2f"))
    print("--------------------------------------")


def main():
    chc = menu()
    size = input("what size (small, medium, large)")
    if chc == 1:
      price=  brewedPrice(size)
    elif chc ==2:
        price= lattePrice(size)

    tax = computetax(price)
    printResults(price,tax)


main()
       
