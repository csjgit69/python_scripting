"""
week for lessions/examples
"""
import math
import datetime
import random

def mod1():
    # Constants
    print("Math constants")
    print("==============")
    print(math.pi)
    print(math.e)
    print("")

    # Functions
    print("Math functions")
    print("==============")
    print(math.sqrt(25))
    print(math.trunc(14.83483))
    print(math.sin(math.pi / 2.0))
    print("")

    # Dir
    print("Dir")
    print("===")
    print(dir(math))
    print("")

    print(math.__name__)
    return 0

def dates():
    # Create some dates
    print("Creating Dates")
    print("==============")
    date1 = datetime.date(1999, 12, 31)
    date2 = datetime.date(2000, 1, 1)
    date3 = datetime.date(2016, 4, 15)
    # date4 = datetime.date(2012, 8, 32)
    # Today's date
    today = datetime.date.today()
    print(today)
    print(date1)
    print(date2)
    print(date3)
    print("")

    # Compare dates
    print("Comparing Dates")
    print("===============")

    print(date1 < date2)
    print(date3 <= date1)
    print(date2 == date3)

    print("")

    # Subtracting dates
    print("Subtracting Dates")
    print("=================")

    diff = date2 - date1
    print(diff)
    print(diff.days)

    diff2 = date3 - date2
    print(diff2)
    print(diff2.days)

    print("")
    return 0


"""
Implementing RPSLS for Practice Project
"""
"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# In this expanded list, each choice wins against the preceding two choices and loses against the following two choices
# (if rock and scissors are thought of as being adjacent using modular arithmetic).
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4
    corresponding to numbering in video
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    return "Bad choice"


def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "lizard"
    elif number == 3:
        return "scissors"
    return "Invalid Number"


def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS
    and print results to console
    """
    # print a blank line to separate consecutive games
    # print out the message for the player's choice
    # convert the player's choice to player_number using the function name_to_number()
    # compute random guess for comp_number using random.randrange()
    # convert comp_number to comp_choice using the function number_to_name()
    # print out message for computer's choice
    # compute difference of player_number and comp_number modulo five
    # use if/elif/else to determine winner and print winner message
    print("")
    # name_to_number(input("New Game, enter your choice:"))
    comp_num = random.randrange(0,3)
    print("Player chooses ",player_choice)
    print("Computer chooses ",number_to_name(comp_num))
    winner = name_to_number(player_choice) - comp_num
    print("winner = ",winner," modulo 5 = ",winner%5)
    if winner == 0:
        print("Player and computer tie!")
    if winner == 1 or winner == 2:
        print("Player Wins!")
    else:
        print("Computer Wins!")
    pass

def rpsls_test():
    # test your code
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
    # print("0-4 ",0-4," ",(0-4)%5)
    # print("0-3 ",0-3," ",(0-3)%5)
    # print("1-0 ",1-0," ",(1-0)%5)
    # print("1-4 ",1-4," ",(1-4)%5)
    # print("4-2 ",4-2," ",(4-2)%5)
    # print("4-3 ",4-3," ",(4-3)%5)


# always remember to check your completed program against the grading rubric


def main():
    # mod1()
    # dates()
    rpsls_test()


if __name__ == "__main__":
    main()


