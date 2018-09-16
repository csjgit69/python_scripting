"""
Week 2 practice project solution for Python Data Visualization
Compute county centers from an SVG image of USA that includes county boundaries
Output a CSV file with FIPS code and county centers
"""

import math
import csv
from xml.dom import minidom
import time
import random
import csv

def ex_sets():
    """
    Using sets.
    """
    print("Set Literals")
    print("============")
    numbers = {3, 2, 1, 4}
    print(numbers)
    letters = {"a", "b", "a", "c", "b"}
    print(letters)
    empty = {}
    print(empty, type(empty))
    empty2 = set()
    print(empty2, type(empty2))
    set1 = set([3, 1, 1, 3, 6, 5])
    print(set1)
    set2 = set(range(5))
    print(set2)
    print("")
    print("Adding/Removing Elements")
    print("========================")
    set1.add(10)
    print(set1)
    element = set1.pop()
    print(element)
    print(set1)
    set1.discard(3)
    print(set1)

    print("")
    print("Set Iteration")
    print("=============")

    for item in letters:
        print(item)

    return


"""
Some sample code illustrating the speed of the "in" operator for lists vs. dictionaries in Python
See https://wiki.python.org/moin/TimeComplexity for more details
"""



def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """

    with open(file_name, newline='') as csv_file:  # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

def test_CSV_join_efficiency(cancer_csv_file, center_csv_file):
    """
    Extract lists of FIPS codes from cancer-risk data set and county center data set
    Measure running time to determine whether FIPS codes in cancer-risk set are in county center set
    """

    # Read in both CSV files
    risk_table = read_csv_file(cancer_csv_file)
    risk_FIPS_list = [risk_table[idx][CANCER_RISK_FIPS_COL] for idx in range(len(risk_table))]
    print("Read", len(risk_FIPS_list), "cancer-risk FIPS codes")

    center_table = read_csv_file(center_csv_file)
    center_FIPS_list = [center_table[idx][CENTER_FIPS_COL] for idx in range(len(center_table))]
    print("Read", len(center_FIPS_list), "county center FIPS codes")

    start_time = time.time()
    for code in risk_FIPS_list:
        if code in center_FIPS_list:
            pass
    end_time = time.time()
    print("Checked for FIPS membership using list in", end_time - start_time, "seconds")

    center_FIPS_dict = {code: True for code in center_FIPS_list}
    start_time = time.time()
    for code in risk_FIPS_list:
        if code in center_FIPS_dict:
            pass
    end_time = time.time()
    print("Checked for FIPS membership using dict in", end_time - start_time, "seconds")



def test_membership_efficiency():
    """
    Test the efficiency of the "in" operator on list/dictionaries of larger size
    """
    test_list = list(range(0, TEST_SIZE, TEST_STRIDE))  # Convert range() to list, membership in range is fast
    test_dict = {idx: True for idx in test_list}

    print()

    # Code to test efficiency of "in" for lists
    start_time = time.time()
    for idx in range(TEST_SIZE):
        if idx in test_list:  # "in" operation iterates through entire list to check membership
            pass
    end_time = time.time()
    print("Total time for", TEST_SIZE, "membership test for list is", end_time - start_time, "seconds")

    # Code to test efficiency of "in" for dicts
    start_time = time.time()
    for idx in range(TEST_SIZE):
        if idx in test_dict:  # "in" operations does NOT iterate through dictionary to check membership
            pass
    end_time = time.time()
    print("Total time for", TEST_SIZE, "membership test for dict is", end_time - start_time, "seconds")


CANCER_RISK_FIPS_COL = 2
CENTER_FIPS_COL = 0
TEST_SIZE = 20000000
TEST_STRIDE = 3


def main():
    """
    main body of script
    :return:
    """
    # ex_sets()

    test_CSV_join_efficiency("cancer_risk_trimmed_solution.csv", "USA_Counties_with_FIPS_and_centers.csv")

    # Code that test the efficiency of "in" operator on larger examples

    test_membership_efficiency()


if __name__ == "__main__":
    main()

                    

