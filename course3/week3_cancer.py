"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""
#########################################################
# Part 1 - Week 3

import csv
import logging

# global logger for turning debug on/off
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig( # filename = "test_log.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode='w')                       # overwrite log file
logger = logging.getLogger()


def print_table(table):
    """
    Echo a nested list to the console
    """
    print()
    print("In print_table")
    logger.info("Debug message, in print_table")
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """

    def read_csv_fieldnames(filename, separator, quote):
        """
        Inputs:
          filename  - name of CSV file
          separator - character that separates fields
          quote     - character used to optionally quote fields
        Output:
          A list of strings corresponding to the field names in
          the given CSV file.
        """
        return

    print()
    csv_table = []

    with open(file_name, newline='') as csvfile:
        filein = csv.DictReader(csvfile)
        print("***************")
        print(filein.fieldnames)
        print("***************")
        for row in filein:
            print(row)
            csv_table.append(row)

    # with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
    #     csv_reader = csv.reader(csv_file, delimiter=",")
    #     for row in csv_reader:
    #         print(row)
    #         csv_table.append(row)


    return csv_table



def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """

    pass

        
def test_part1_code():
    """
    Run examples that test the functions for part 1
    """
    
    # Simple test for reader
    test_table = read_csv_file("test_case.csv")  # create a small CSV for this test

    print("read test")
    print(test_table)
    print()

    # Test the writer
    # cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    # write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
    # cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")
    
    # Test whether two tables are the same
    pass

def main():

    test_part1_code()


if __name__ == "main()":
    main()