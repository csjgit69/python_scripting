"""
Boolean logic in Python
"""

def boolean_play():
    val1 = True
    val2 = False
    print("Not of ",val1, " is: ",not val1)
    return 0

def comp_ops():
    print("Comparisons")
    print("===========")
    print("7 > 3: ",7 > 3)
    print("7 < 3: ",7 < 3)
    print("7 >= 3: ",7 >= 3)
    print("7 <= 3: ",7 <= 3)
    print("7 == 3: ",7 == 3)
    print("7 != 3: ",7 != 3)

    # == and != are also useful for non-numeric types
    print("Comparing Strings")
    print("=================")
    name = 'Scott'
    equal = name != "Joe"
    print("equal = name[",name,"] != \"Joe\": ",equal)

    print("")
    return 0

def greet(friend, money):
    """
    Greet people. Say hi if they are ayourfriend and give them $20 if you have enough money
    :param friend:
    :param money:
    :return:
    """
    if friend and (money>=20):
        print("Hi friend!")
        money -= 20
    elif friend:
        print("Hello friend.")
    else:
        print("Ha Ha!")
        money += 10
    return money

def main():
    # boolean_play()
    # comp_ops()
    money = 10
    money = greet(False,money)
    print("Money:",money)
    money = greet(True,money)
    print("Money:",money)
    money = greet(True,money)
    print("Money:",money)
    print("a">"A")
    print(greet.__doc__)

    


if __name__ == '__main__':
  main()
