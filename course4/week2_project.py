"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal




def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output:
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    gdp_years = {}
    gdp_table = []
    # get all the tupple par data out of dgpdata, some with be in the form (year, gdpval)
    # some won't if both values in the tupple par are numbers then store them in a list
    for year,gdpval in gdpdata.items():
        print("year, gdpval: ", year, gdpval)
        try:
            gdp_years[int(year)] = float(gdpval)
        except ValueError:
            pass

        # if (year.isdigit() and gdpval.isdigit()):
        #     gdp_years[int(year)] = float(gdpval)
    print()
    print("gdp_years list: ")
    print(gdp_years)

    for year in range(gdpinfo["min_year"],gdpinfo["max_year"]+1):
        # print("in year range, year: ", year)
        if year in gdp_years:
            gdp_table.append((year, gdp_years[year]))
    print()
    print("gdp_table: ")
    print(gdp_table)

    return gdp_table


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    gdp_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],
                                       gdpinfo["separator"], gdpinfo["quote"])
    plot_dict = {}
    for country in country_list:
        if country in gdp_dict:
            gdpdata = gdp_dict[country]
            print("country: ", gdpdata)
            plot_dict[country] = (build_plot_values(gdpinfo, gdpdata))
        else:
            plot_dict[country] = []
    print()
    print("Country plot dict, keys: ", country_list)
    print(plot_dict)
    print()
    return plot_dict


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    return


def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    # gdpinfo = {
    #     # "gdpfile": "isp_gdp.csv",
    #     "gdpfile": "gdptable1.csv",
    #     "separator": ",",
    #     "quote": '"',
    #     "min_year": 1960,
    #     "max_year": 2015,
    #     "country_name": "Country Name",
    #     "country_code": "Country Code"
    # }
    # build_plot_values({'country_name': 'Country Name', 'min_year': 1980, 'separator': '',
    #                    'max_year': 2000, 'country_code': 'Code', 'quote': '', 'gdpfile': ''},
    #                   {'1997': '753.3', '2000': '238489.38538', '1998': '8283.2673',
    #                    '1999': '138013.52'})
    # expected[(1997, 753.3), (1998, 8283.2673), (1999, 138013.52), (2000, 238489.38538)]

    # print("read csv returned:")
    # print(test_dict)
    # build_plot_dict(gdpinfo, ['Country1', 'Country2'])

    # render_xy_plot(gdpinfo, ['Country1', 'Country2'], gdpinfo["gdpfile"])

    # test_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],
    #                                     gdpinfo["separator"], gdpinfo["quote"])
    # print("read csv returned:")
    # print(test_dict)

    # build_plot_dict({'separator': ',', 'min_year': 2000, 'quote': '"',
    #                  'country_name': 'Country Name', 'gdpfile': 'gdptable1.csv',
    #                  'country_code': 'Code', 'max_year': 2005}, ['Country3'])
    # expected
    # {'Country3': []}

    # build_plot_values({'separator': '', 'min_year': 2001, 'quote': '',
    #                    'country_name': 'Country Name', 'gdpfile': '',
    #                    'country_code': 'Code', 'max_year': 2015},
    #                   {'2007': '', '2003': '2', '2015': '14', '2009': '8', '2008': '7',
    #                    '2012': '11', '2006': '5', '2002': '1', '2001': '', '2004': '',
    #                    '2005': '4', '2010': '', '2014': '13', '2013': '', '2011': '10'})
    # expected[(2002, 1.0), (2003, 2.0), (2005, 4.0), (2006, 5.0), (2008, 7.0),
    #          (2009, 8.0), (2011, 10.0), (2012, 11.0), (2014, 13.0), (2015, 14.0)]

    # render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    # render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    # render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
    #                 "isp_gdp_xy_uk+usa.svg")


def main():
    """
    main body function
    :return:
    # Make sure the following call to test_render_xy_plot is commented out
    # when submitting to OwlTest/CourseraTest.
    """
    # test_render_xy_plot()
    #
    # gdpinfo = {
    #     # "gdpfile": "isp_gdp.csv",
    #     "gdpfile": "gdptable1.csv",
    #     "separator": ",",
    #     "quote": '"',
    #     "min_year": 1960,
    #     "max_year": 2015,
    #     "country_name": "Country Name",
    #     "country_code": "Country Code"
    # }


if __name__ == "__main__":
    main()

# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

# test_render_xy_plot()