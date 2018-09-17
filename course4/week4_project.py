"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
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

def read_csv_file(file_name, separator, quote=""):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """
    # don't need to explicitly close the file now
    with open(file_name, newline='') as csv_file:
        csv_table = []
        # csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote )
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

def build_country_code_converter(codeinfo):
    """
    Inputs
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """

    #     codeinfo = {
    #     "codefile": "isp_country_codes.csv",
    #     "separator": ",",
    #     "quote": '"',
    #     "plot_codes": "ISO3166-1-Alpha-2",
    #     "data_codes": "ISO3166-1-Alpha-3"
    # }

    # read_csv_fieldnames(filename, separator, quote=None)

    plot_cvs = read_csv_file(codeinfo["codefile"], codeinfo["separator"], codeinfo["quote"])

    print()
    print("table header row: ")
    print(plot_cvs[0])

    key_col = plot_cvs[0].index(codeinfo["plot_codes"])
    data_col = plot_cvs[0].index(codeinfo["data_codes"])

    print("table: ", plot_cvs[0], " key_col: ", key_col, " data_col: ", data_col)
    code_dict = {}
    for row in plot_cvs[1:]:
        # print()
        # print("table item: ", row, " item[key_col]: ", row[key_col],
        #       " item[data_col]: ", row[data_col])
        code_dict[row[key_col]] = row[data_col]

    print("code_dict: ")
    print(code_dict)

    return code_dict

def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    print()
    print("plot countries: ")
    print(plot_countries)
    print()
    print("gdp_countries : ")
    print(gdp_countries)

    code_map = build_country_code_converter(codeinfo)
    code_map_lower = {}
    for key, val in code_map.items():
        code_map_lower[key.lower()] = val

    plot_map = {}
    plot_errors = set()
    print()
    print("code_map: ")
    print(code_map)
    for code, country in plot_countries.items():
        print()
        print("plot_country code: ", code)
        print("plot_country name: ", country)
        if code.lower() in code_map_lower.keys():
            plot_map[code] = code_map_lower[code]
        else:
            plot_errors.add(code)

    print()
    print("plot_map: ")
    print(plot_map)
    print("plot_errors: ")
    print(plot_errors)


    return plot_map, plot_errors

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    return {}, set(), set()

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    return

def test_render_world_map():
    """
    Test the project code for several years
    """
    print("fuck me now")

    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # build_country_code_converter({'quote': "'", 'data_codes': 'Code2',
    #                               'separator': ',', 'plot_codes': 'Code1',
    #                               'codefile': 'code1.csv'},)
    # expected {'MN': 'OP', 'Ab': 'Cd', 'ST': 'UV', 'Gh': 'Ij'}
    # but received (Exception: ValueError)
    # "'Code1' is not in list" at line 108, in build_country_code_converter

    reconcile_countries_by_code({'plot_codes': 'ISO3166-1-Alpha-2', 'data_codes': 'ISO3166-1-Alpha-3',
                                 'quote': '"', 'separator': ',', 'codefile': 'code4.csv'},
                                {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'},
                                {'USA': {'Country Code': 'USA', 'Country Name': 'United States'},
                                 'NOR': {'Country Code': 'NOR', 'Country Name': 'Norway'},
                                 'PRI': {'Country Code': 'PRI', 'Country Name': 'Puerto Rico'}})
    # expected ({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'},
    #           set()) but received ({}, set()) (Exception: Invalid Keys)
    # Expected dictionary {'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}
    # has a different number of keys than received dictionary {}



    # # 1960
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")
    # # 1980
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")
    # # 2000
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")
    # # 2010
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")

    return

def main():
    """
    main body
    Make sure the following call to test_render_world_map is commented
    out when submitting to OwlTest/CourseraTest.
    :return:
    """
    test_render_world_map()

if __name__ == "__main__":
    main()
