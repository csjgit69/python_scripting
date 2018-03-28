"""
Course2 week three lessions and examples
"""

def list_ex1():
    """
    Mutating Lists.
    """

    print("Updating Items")
    print("==============")

    lst = list(range(5))
    print(lst)

    lst[1] = -7
    lst[3] = 17
    print(lst)

    print("")
    print("Adding Items")
    print("============")

    lst.append(42)
    print(lst)

    lst.insert(2, 75)
    print(lst)

    lst2 = [-56, 27, 8]
    lst.extend(lst2)
    print(lst)
    lst.append(lst2)
    print(lst)

    print("")
    print("Removing Items")
    print("==============")

    lst.pop()
    print(lst)
    lst.pop(3)
    print(lst)
    return 0

def tuple_ex1():
    """
    Tuple examples.
    """

    # Lists and tuples are both sequences
    print("Sequences")
    print("=========")
    lst = [1, 5, 7, 3]
    tup = (1, 5, 7, 3)

    print(lst, tup)
    print(lst[2])
    print(tup[2])
    print(tup[:2])
    print(tup[2:3])

    # Tuples are immutable
    lst[0] = 9
    print(lst)
    # tup[0] = 9
    # print(tup)

    print("")
    print("Tuple Methods")
    print("=============")

    print(tup.index(7))
    print(tup.count(2))

    print("")
    print("Iteration")
    print("=========")

    for item in tup:
        print(item)

    print("")
    print("Conversion")
    print("==========")

    lst2 = [8, 6, 4, 8, 2]
    print(lst2)
    tup2 = tuple(lst2)
    print(tup2)
    # tup2[3] = 7
    lst3 = list(tup2)
    print(lst3)
    lst3[2] = 7
    print(lst2, tup2, lst3)
    return 0

def ref_ex1():
    """
    List Objects and References.
    """

    print("Look Alikes")
    print("===========")

    lst1 = [7, 3, 2]
    lst2 = [7, 3, 2]
    print(lst1, lst2)

    lst1[1] = -8
    print(lst1, lst2)

    print("")
    print("Aliases")
    print("=======")

    lst3 = [1, 5, 9]
    lst4 = lst3
    print(lst3, lst4)

    lst3[1] = 17
    print(lst3, lst4)

    print("")
    print("Copies")
    print("======")

    lst5 = [8, 9, 4]
    # This makes a shallow copy
    lst6 = list(lst5)
    print(lst5, lst6)

    lst5[1] = -2
    print(lst5, lst6)

    print("")
    print("Function Arguments")
    print("==================")


    lst7 = [1, 2, 3]
    print(lst7)
    mutate_list(lst7)
    print(lst7)
    return 0

def mutate_list(alist):
    """
    Add an element to the input.
    """
    alist.append(42)

def ref_ex2():
    """
    Some simple examples of reference issues for lists
    """

    print ("Part 1 - references to two distinct objects")
    iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
    iipp2_instructors = ["Joe", "Scott", "John", "Stephen"]
    print(iipp1_instructors)
    print(iipp2_instructors)

    print ("Mutate one of the two objects")
    iipp2_instructors.pop()
    print(iipp1_instructors)
    print(iipp2_instructors)
    print()

    print ("Part 2 - two references to the same object")
    iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
    iipp2_instructors = iipp1_instructors
    print(iipp1_instructors)
    print(iipp2_instructors)

    print ("Mutate the object")
    iipp2_instructors.pop()
    print(iipp1_instructors)
    print(iipp2_instructors)
    print()

    print ("Part 3 - two references to an object and a copy of the object")
    iipp1_instructors = ["Joe", "Scott", "John", "Stephen"]
    iipp2_instructors = list(iipp1_instructors)
    print(iipp1_instructors)
    print(iipp2_instructors)

    print ("Mutate the one of the objects")
    iipp2_instructors.pop()
    print(iipp1_instructors)
    print(iipp2_instructors)
    return 0

def main():
    """
    main program to keep test and functions clean
    :return:
    """
    # list_ex1()
    # tuple_ex1()
    # ref_ex1()
    ref_ex2()


if __name__ == "__main__":
    main()


