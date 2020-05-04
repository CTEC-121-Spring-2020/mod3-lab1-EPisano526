"""
CTEC 121
Esther Pisano
module 3 lab 1
chapter 7 material
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    # conditional expressions
    '''
    # literal
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    # relational opterators
    print("Relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3== 3", 3 == 3)
    print("3 >=5", 3 <= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variable
    x = 3
    y = 5
    print("Using variables")
    print("x:", x, "y:", y)
    print("x <y", x < y)
    print("x != y", x != y)
    print()

    # simple if statement
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statement
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x< y")
    else:
        print("x >= y")

    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x< y")
    else:
        print("x >= y")

    print("end if/else example")
    print()

    # Determining if a number is odd or even
    for range(1-10)
        if list((range((1-10) % 2) == 0:
            print("number is even")
        else list((1-10) % 2 != 0:
            print("number is odd")

    for i in range(1, 11):
        if (i % 2) == 0:
            outputString = "even"
        else:
            outputString = "odd"
        print(i, outputString)
    print()

    # alph names
    name = "Bill"
    firstLetterOfName = "B"

    print("Multi-way if example")
    if firstLetterOfName == "A":
        print(name)
    elif firstLetterOfName == "B":
        print("B")
    elif firstLetterOfName == "C":
        print(name)
    # ...
    elif firstLetterOfName == "Y":
        print(name)
    else:       # default case: name starts with Z
        print(name)
    print()
    '''
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. ")
        exit()


main()
