"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

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

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    country_map = {}
    missing_set = set()
    for c_code, country in plot_countries.items():
        if country in gdp_countries.keys():
            country_map[c_code] = country
        else:
            missing_set.add(c_code)
    print()
    print("Code_map size: ", len(country_map))
    print(country_map)
    print()
    print("Missing_set size: ", len(missing_set))
    print(missing_set)
    print()

    return country_map, missing_set

def get_year_val(gdp_year, gdpdata):
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
    gdp_table = ()
    # get all the tupple par data out of dgpdata, some with be in the form (year, gdpval)
    # some won't if both values in the tupple par are numbers then store them in a list
    for year,gdpval in gdpdata.items():
        # print("year, gdpval: ", year, gdpval)
        try:
            gdp_years[int(year)] = float(gdpval)
        except ValueError:
            pass

        # if (year.isdigit() and gdpval.isdigit()):
        #     gdp_years[int(year)] = float(gdpval)
    print()
    print("gdp_years list: ")
    print(gdp_years)
    print()
    print("gdp year: ", gdp_year)
    if gdp_year in gdp_years:
        gdp_table = (gdp_year, gdp_years[gdp_year])
    print()
    print("gdp_table: ")
    print(gdp_table)

    return gdp_table

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    # pygal_countries = pygal.maps.world.COUNTRIES
    gdp_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],
                                       gdpinfo["separator"], gdpinfo["quote"])
    code_map, country_missing = reconcile_countries_by_name(plot_countries,gdp_dict)
    country_map ={}
    gdp_missing = set()

    for c_code, country in code_map.items():
        gdp_tup = get_year_val(int(year), gdp_dict[country])
        print("c_code: ", c_code, " len(gdp_tuple): ", len(gdp_tup), " gdp_tuple: ", gdp_tup)
        if len(gdp_tup) > 0:
            print("country: ", country, " year: ", year, " gdp: ", gdp_tup)
            print("t_year: ", gdp_tup[0], " t_gdp: ", gdp_tup[1])
            country_map[c_code] = math.log10(gdp_tup[1])
        else:
            gdp_missing.add(c_code)

    print()
    print("country_map: ")
    print(country_map)
    print()
    print("country_missing set: ")
    print(country_missing)
    print()
    print("gdp_missing set: ")
    print(gdp_missing)

    return country_map, country_missing, gdp_missing

def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    return

def test_render_world_map():
    """
    Test the project code for several years.
    """
    # gdpinfo = {
    #     "gdpfile": "isp_gdp.csv",
    #     # "gdpfile": "gdptable1.csv",
    #     "separator": ",",
    #     "quote": '"',
    #     "min_year": 1960,
    #     "max_year": 2015,
    #     "country_name": "Country Name",
    #     "country_code": "Country Code"
    # }
    # Get pygal country code map
    # pygal_countries = pygal.maps.world.COUNTRIES
    #
    # gdp_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],
    #                                     gdpinfo["separator"], gdpinfo["quote"])
    #
    # reconcile_countries_by_name(pygal_countries,gdp_dict)
    # reconcile_countries_by_name({'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'},
    #                             {'Norway': {'Country Code': 'NOR', 'Country Name': 'Norway'},
    #                              'United States': {'Country Code': 'USA',
    #                                                'Country Name': 'United States'}})
    # expected ({'no': 'Norway', 'us': 'United States'}, {'pr'})
    # but received ({'no': 'Norway', 'us': 'United States'}, {'Puerto Rico'})

    build_map_dict_by_name({'separator': ',', 'min_year': 2000, 'quote': '"',
                            'country_name': 'Country Name','gdpfile': 'gdptable1.csv',
                            'country_code': 'Code', 'max_year': 2005},
                           {'C3': 'Country3', 'C5': 'Country5', 'C1': 'Country1',
                            'C4': 'Country4','C2': 'Country2'}, '2003')
    # expected ({'C1': 0.6020599913279623, 'C2': 1.1139433523068367},
    #           {'C3', 'C5', 'C4'}, set())
    # but received ({}, set(), set()) (Exception: Invalid Keys)
    # Expected dictionary {'C1': 0.6020599913279623, 'C2': 1.1139433523068367}
    # has a different number of keys than received dictionary {}


    # code_map, missing_set = reconcile_countries_by_name(pygal_countries,gdp_dict)
    # build_map_dict_by_name(gdpinfo, code_map, 2000)

    # # 1960
    # render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")
    # # 1980
    # render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")
    # # 2000
    # render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")
    # # 2010
    # render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")

    return

def main():
    """
    main body
    :return:
    """

    print("fuck this fucking shit")
    test_render_world_map()

if __name__ == "__main__":
    main()

# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

