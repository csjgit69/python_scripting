"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""
#########################################################
# Part 1 - Week 3

import csv
import logging

# # global logger for turning debug on/off
# LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# logging.basicConfig( # filename = "test_log.log",
#                     level = logging.DEBUG,
#                     format = LOG_FORMAT,
#                     filemode='w')                       # overwrite log file
# logger = logging.getLogger()


# def print_table(table):
#     """
#     Echo a nested list to the console
#     """
#     print()
#     print("In print_table")
#     logger.info("Debug message, in print_table")
#     for row in table:
#         print(row)

def read_csv_fieldnames(filename, separator, quote=None):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    with open(filename, newline='') as csvfile:
        if quote:
            filein = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        else:
            filein = csv.DictReader(csvfile, delimiter=separator)
        # print("***************")
        # print(filein.fieldnames)
        # print("***************")
        return filein.fieldnames

def read_csv_as_list_dict(filename, separator, quote=None):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    dict_list = []
    with open(filename, newline='') as csvfile:
        if quote:
            filein = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        else:
            filein = csv.DictReader(csvfile, delimiter=separator)
        for row in filein:
            # print("***************")
            # print("list of dicts: ")
            # print(dict(row))
            # print("***************")
            dict_list.append(dict(row))
    # print("finished list: ", dict_list)

    return dict_list


def read_csv_as_nested_dict(filename, keyfield, separator, quote=None):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    csv_dict = {}
    with open(filename, newline='') as csvfile:
        if quote:
            filein = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        else:
            filein = csv.DictReader(csvfile, delimiter=separator)
        for row in filein:
            print("***************")
            print("row in nested dicts of dicts: ")
            print(keyfield[0])
            # if (len(keyfield) > 1):
            #     row_name = row[keyfield[0]]
            # else:
            #     row_name = keyfield
            # print(row_name)
            csv_dict[row[keyfield]]=(dict(row))
            print("***************")
    print("finished list: ", csv_dict)

    return csv_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """

    with open(filename, "w", newline='') as csvfile:
        if quote:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator,
                                    quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        else:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=separator,
                                    quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
        print("===============")
        print(fieldnames)
        print("===============")
        writer.writeheader()
        for row in table:
            writer.writerow(row)


def test_funcs_code():
    """
    Run examples that test the functions for part 1
    """
    
    # Simple test for reader
    col_names = read_csv_fieldnames("table1.csv", ",")
    print("***************")
    print("column names: ", col_names)
    print("***************")

    test_dict = read_csv_as_list_dict("table1.csv", ",")
    print("***************")
    print("test list of dictionaries: ")
    print(test_dict)
    print("***************")

    write_csv_from_list_dict("test_out.csv", test_dict, col_names, "'", csv.QUOTE_MINIMAL)
    write_csv_from_list_dict('test_out.csv', [{'b': 11, 'd': 13, 'e': 14, 'c': 12, 'a': 10},
                                              {'b': 21, 'd': 23, 'e': 24, 'c': 22, 'a': 20},
                                              {'b': 31, 'd': 33, 'e': 34, 'c': 32, 'a': 30},
                                              {'b': 41, 'd': 43, 'e': 44, 'c': 42, 'a': 40}],
                                              ['a', 'b', 'c', 'd', 'e'], ',', '"')

    col_names = read_csv_fieldnames("table1.csv", ",")
    test_dict = read_csv_as_nested_dict("table1.csv", col_names[0], ",", '"')
    test_dict = read_csv_as_nested_dict("table1.csv", col_names[3], ",", '"')
    print("***************")
    print("test dict of dictionaries: ")
    print(test_dict)
    print("***************")

    # Test the writer
    # cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    # write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
    # cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")
    
    # Test whether two tables are the same

def main():
    """
    Main function, it all starts here
    :return:
    """



    print("fuck me")
    test_funcs_code()


if __name__ == "__main__":
    main()