"""
Course3 week one lessions and examples
"""
import os
import csv

def csv_ex1():
    """
    Example code to read and parse a CSV file.
    """
    def parse(csvfilename):
        """
        Reads CSV file named csvfilename, parses
        it's content and returns the data within
        the file as a list of lists.
        """
        table = []
        with open(csvfilename, "r") as csvfile:
            for line in csvfile:
                line = line.rstrip()
                columns = line.split(',')
                table.append(columns)
        return 0


    def print_table(table):
        """
        Print out table, which must be a list
        of lists, in a nicely formatted way.
        """
        for row in table:
            # Header column left justified
            print("{:<19}".format(row[0]), end='')
            # Remaining columns right justified
            for col in row[1:]:
                print("{:>4}".format(col), end='')
            print("", end='\n')
        return 0

    table = parse("hightemp.csv")
    print_table(table)

    print("")
    print("")

    table2 = parse("hightemp2.csv")
    print_table(table2)
    return 0

def csv_ex2():
    """
    Using the csv module.
    """
    def parse(csvfilename):
        """
        Reads CSV file named csvfilename, parses
        it's content and returns the data within
        the file as a list of lists.
        """
        table = []
        with open(csvfilename, "r") as csvfile:
            csvreader = csv.reader(csvfile,
                                   skipinitialspace=True)
            for row in csvreader:
                table.append(row)
        return table


    def print_table(table):
        """
        Print out table, which must be a list
        of lists, in a nicely formatted way.
        """
        for row in table:
            # Header column left justified
            print("{:<19}".format(row[0]), end='')
            # Remaining columns right justified
            for col in row[1:]:
                print("{:>4}".format(col), end='')
            print("", end='\n')
        return 0

    table = parse("hightemp.csv")
    print_table(table)

    print("")
    print("")

    table2 = parse("hightemp2.csv")
    print_table(table2)

    return 0

def csv_ex3():
    """
    Using csv.DictReader.
    """
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec')

    def dictparse(csvfilename, keyfield):
        """
        Reads CSV file named csvfilename, parses
        it's content and returns the data within
        the file as a dictionary of dictionaries.
        """
        table = {}
        # newline = '' tells Python not to process newlines and lets the csv reader handle them
        # this let's newlines occur inside values in the table. csv reader is built to handle this correctly, Python is not
        with open(csvfilename, "rt", newline='') as csvfile:
            csvreader = csv.DictReader(csvfile,
                                       skipinitialspace=True)
            for row in csvreader:
                table[row[keyfield]] = row
        return table


    def print_table(table):
        """
        Print out table, which must be a dictionary
        of dictionaries, in a nicely formatted way.
        """
        print("City               ", end='')
        for month in MONTHS:
            print("{:>6}".format(month), end='')
        print("")
        for name, row in table.items():
            # Header column left justified
            print("{:<19}".format(name), end='')
            # Remaining columns right justified
            for month in MONTHS:
                print("{:>6}".format(row[month]), end='')
            print("", end='\n')

    table = dictparse("hightemp.csv", 'City')
    print_table(table)
    return 0

def csv_ex4():
    """
    CSV reader options.
    """
    def dictparse(csvfilename, keyfield, separator, quote, quotestrategy):
        """
        Reads CSV file named csvfilename, parses
        it's content and returns the data within
        the file as a dictionary of dictionaries.
        """
        table = {}
        with open(csvfilename, "rt", newline='') as csvfile:
            csvreader = csv.DictReader(csvfile,
                                       skipinitialspace=True,
                                       delimiter=separator,
                                       quotechar=quote,
                                       quoting=quotestrategy)
            for row in csvreader:
                table[row[keyfield]] = row
        return table, csvreader.fieldnames

    def print_table(table, fieldnames):
        """
        Print out table, which must be a dictionary
        of dictionaries, in a nicely formatted way.
        """
        print("{:<19}".format(fieldnames[0]), end='')
        for field in fieldnames[1:]:
            print("{:>6}".format(field), end='')
        print("")
        for name, row in table.items():
            # Header column left justified
            print("{:<19}".format(name), end='')
            # Remaining columns right justified
            for field in fieldnames[1:]:
                print("{:>6}".format(row[field]), end='')
            print("", end='\n')

    table, fieldnames = dictparse("hightemp.csv", 'City', ',', '"', csv.QUOTE_MINIMAL)
    print(fieldnames)
    print_table(table, fieldnames)

    print("")
    print("")

    table2, fieldnames2 = dictparse("hightemp2.csv", 'City', ',', '"', csv.QUOTE_NONNUMERIC)
    print_table(table2, fieldnames2)

    print("")
    print("")

    table3, fieldnames3 = dictparse("hightemp3.csv", 'City', ' ', "'", csv.QUOTE_NONNUMERIC)
    print_table(table3, fieldnames3)
    return 0

def csv_ex5():
    """
    Examples code for experimenting with options to the csv.read() and csv.write() methods
    """
    # Function that prints 2D table to console

    def print_table(table):
        """
        Echo a nested list to the console
        """
        for row in table:
            print(row)


    # Options for reading a CSV file

    def read_csv_file(file_name, file_delimeter):
        """
        Given a CSV file path and a delimiter as strings,
        read the data into a 2D table and return the table
        """

        with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
            csv_table = []
            csv_reader = csv.reader(csv_file, delimiter=file_delimeter)
            for row in csv_reader:
                csv_table.append(row)
        return csv_table


    def csv_delimiter_examples():
        """
        Run some example of reading CSV files using different delimiter options
        """
        number_table = read_csv_file("number_table.csv", " ")
        print_table(number_table)
        print()
        name_table = read_csv_file("name_table.csv", ",")
        print_table(name_table)

    csv_delimiter_examples()

    # Options for writing a CSV file

    def write_csv_file(csv_table, file_name, file_delimiter, quoting_value):
        """
        Given a nested list csv_table, write the data into a
        CSV file with the name file_name
        """

        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=file_delimiter, quoting=quoting_value)
            for row in csv_table:
                csv_writer.writerow(row)

    def csv_quoting_examples():
        """
        Run some example of writing 2D tables as CSV files using various quoting options
        """
        name_table = read_csv_file("name_table.csv", ",")
        name_table.append([1, 2, 3])
        write_csv_file(name_table, "name_table_minimal.csv", ",", csv.QUOTE_MINIMAL)
        write_csv_file(name_table, "name_table_all.csv", ",", csv.QUOTE_ALL)
        write_csv_file(name_table, "name_table_nonnumeric.csv", ",", csv.QUOTE_NONNUMERIC)
        # This causes errors because quotes are in table and Python gets lost, don't use in general
        #write_csv_file(name_table, "name_table_none.csv", ",", csv.QUOTE_NONE)        # no escapechar is set for lots of quotes



    csv_quoting_examples()
    return 0

def main():
    """
    main program to keep test and functions clean
    :return:
    """

    # csv_ex1()
    # csv_ex2()
    # csv_ex3()
    # csv_ex4()
    csv_ex5()


if __name__ == "__main__":
    main()


