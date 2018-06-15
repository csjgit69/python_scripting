"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

##
## Provided code from Week 3 Project
##

def read_csv_as_list_dict(filename, separator, quote):
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
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
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
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


##
## Part 1: Functions to compute top batting statistics by year
##

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    new_list = []
    # print("year: ",year)
    # print("yearid: ",yearid)
    # print("dic:\n",statistics)
    for dic in statistics:
        # print("dic:  ",type(dic))
        # print("dic[yearid]:  ",dic[yearid])
        if (int(dic[yearid]) == year):
            new_list.append(dic)

    return new_list


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    print()
    print("info:\n", info)
    print()
    print("statistics:\n",statistics)
    print()
    print("formula:",formula,"numplayers:",numplayers)
    print()

    plyr_lst = [] # list of all players in the statistics database
    for players in statistics:
        plyr_lst.append( (players[info["playerid"]],formula(info, players )))

    # print("player list:\n",plyr_lst)
    plyr_lst.sort(key=lambda x:x[1], reverse=True)
    del plyr_lst[numplayers:]
    # print("player list, sorted:\n",plyr_lst)
    return plyr_lst


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    print()
    print("info:\n", info)
    print()
    print("top ids:\n",top_ids_and_stats)

    bb_stats = read_csv_as_list_dict(info["masterfile"], info["separator"],info["quote"])

    name_list = [] # list of batting averages and names in string format
    for ids in top_ids_and_stats:
        for dic in bb_stats:
            if dic[info["playerid"]] == ids[0]:
                f_name = dic[info["firstname"]]
                l_name = dic[info["lastname"]]
                # b_avg = str(ids[1])
                name_list.append("{:.3f} --- {} {}".format(ids[1], f_name, l_name))

    print()
    print("name list:\n",name_list)
    return name_list


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    # print()
    # print("info:\n",info)
    # print()
    # print("formula:\n",formula)
    # print()
    # print("numplayers:\n",numplayers)
    # print()
    # print("year:\n",year)

    # mf_stats = read_csv_as_list_dict(info["masterfile"], info["separator"],info["quote"])
    bf_stats = read_csv_as_list_dict(info["battingfile"], info["separator"],info["quote"])
    bf_stats = filter_by_year(bf_stats,year,info["yearid"])
    bf_stats = top_player_ids(info,bf_stats,formula,numplayers)
    # print()
    # print("mfstats:\n",mf_stats)
    # print()
    # print("bfstats by year:\n",bf_stats)
    top_plys = lookup_player_names(info,bf_stats)
    # print()
    # print("top players by year:\n",top_plys)
    return top_plys

##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    print()
    print("player:\n",playerid)
    print()
    print("fields:\n",fields)
    print()
    print("statistics:\n",statistics)
    agg_dic = {}
    for bat_list in statistics:         # walk through the dictionaries of stats
        key = bat_list.get(playerid)
        # print()
        # print("key:\n",key)
        for stat,val in bat_list.items():
            # print("stat:",stat,val)
            if stat in fields and key not in agg_dic:
                agg_dic[key] = {}
                agg_dic[key][stat] = int(val)
                agg_dic[key][playerid] = key
                # print("if:\n",agg_dic[key][stat])
            elif stat in fields and stat not in agg_dic[key]:
                agg_dic[key][stat] = int(val)
                # print("elif:\n",agg_dic[key][stat])
            elif stat in fields:
                agg_dic[key][stat] = agg_dic[key][stat] + int(val)
                # print("else:\n",agg_dic[key][stat])


    # for plys in statistics:
    #     agg_dic[playerid]
    print("fml:\n",agg_dic)
    return agg_dic


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    Output:
       return a list of strings of the same form as returned by
       lookup_player_names that correspond to the numplayers players
       with the highest compound statistic computed by formula for their careers.
    """

    # mf_stats = read_csv_as_list_dict(info["masterfile"], info["separator"],info["quote"])
    bf_stats = read_csv_as_list_dict(info["battingfile"], info["separator"],info["quote"])

    player_agg = aggregate_by_player_id(bf_stats,info["playerid"],info["battingfields"])
    print()
    print("player agg:\n",player_agg)
    player_stats = []
    for player in player_agg.values():
        player_stats.append(player)

    top_players = top_player_ids(info,player_stats,formula,numplayers)
    print("top players:\n",top_players)

    top_names = lookup_player_names(info,top_players)
    print()
    print("top names:\n",top_names)

    return top_names


##
## Provided testing code
##

def test_baseball_statistics():
    """
    Simple testing code.
    """
    print("")

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    # bb_stats1 = read_csv_as_list_dict("isp_baseball_files/batting1.csv", ",", '"')
    # bb_stats1 = read_csv_as_list_dict("Batting_2016.csv", ",", '"')
    # print("row[yearid]:  ",row[yearid])
    # filter_by_year(bb_stats1, 2021, baseballdatainfo["yearid"])
    # print(bb_stats1)

    print()
    filter_by_year([{'year1': '1', 'year3': '3', 'year2': '2'}], 1, 'year1')
    top_player_ids({'masterfile': '', 'battingfile': '', 'separator': ',', 'quote': '"', \
                   'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', \
                   'yearid': 'year', 'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', \
                   'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks', 'battingfields': \
                   ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']},\

                   [{'doubles': '20', 'hits': '108', 'homers': '5', 'year': '2020', \
                     'player': 'player0', 'triples': '1', 'walks': '25', 'atbats': '300'},\
                    {'doubles': '5', 'hits': '170', 'homers': '4', 'year': '2020',\
                     'player': 'player1', 'triples': '3', 'walks': '10', 'atbats': '499'},\
                    {'doubles': '18', 'hits': '129', 'homers': '20', 'year': '2020',\
                     'player': 'player2', 'triples': '5', 'walks': '85', 'atbats': '513'},\
                    {'doubles': '3', 'hits': '67', 'homers': '22', 'year': '2020',\
                     'player': 'player5', 'triples': '2', 'walks': '37', 'atbats': '197'},\
                    {'doubles': '33', 'hits': '166', 'homers': '18', 'year': '2020',\
                     'player': 'player6', 'triples': '7', 'walks': '25', 'atbats': '542'},\
                    {'doubles': '19', 'hits': '161', 'homers': '10', 'year': '2020',\
                     'player': 'player7', 'triples': '2', 'walks': '27', 'atbats': '500'},\
                    {'doubles': '42', 'hits': '176', 'homers': '25', 'year': '2020',\
                     'player': 'player8', 'triples': '13', 'walks': '30', 'atbats': '589'}],\
                    batting_average, 1)

    lookup_player_names({'masterfile': 'isp_baseball_files/master1.csv', 'battingfile': '',\
                         'separator': ',', 'quote': '"', 'playerid': 'player',\
                         'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',\
                         'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles',\
                         'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',\
                         'battingfields': ['atbats', 'hits', 'doubles', 'triples',\
                         'homers', 'walks']},[('player0', 0.1)])

    compute_top_stats_year({'masterfile': 'isp_baseball_files/master1.csv',\
                            'battingfile': 'isp_baseball_files/batting1.csv',\
                            'separator': ',', 'quote': '"', 'playerid': 'player',\
                            'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',\
                            'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles',\
                            'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',\
                            'battingfields': ['atbats', 'hits', 'doubles', 'triples',\
                                              'homers', 'walks']}, batting_average, 3, 2020)

    aggregate_by_player_id([{'stat1': '3', 'stat2': '4', 'player': '1', 'stat3': '5'},\
                            {'stat1': '2', 'stat2': '1', 'player': '1', 'stat3': '8'},\
                            {'stat1': '5', 'stat2': '7', 'player': '1', 'stat3': '4'}],\
                           'player', ['stat1'])

    compute_top_stats_career({'masterfile': 'isp_baseball_files/master1.csv',\
                              'battingfile': 'isp_baseball_files/batting1.csv',\
                              'separator': ',', 'quote': '"', 'playerid': 'player',\
                              'firstname': 'firstname', 'lastname': 'lastname',\
                              'yearid': 'year', 'atbats': 'atbats', 'hits': 'hits',\
                              'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers',\
                              'walks': 'walks',\
                              'battingfields': ['atbats', 'hits', 'doubles', 'triples',\
                                                'homers', 'walks']}, batting_average, 4)

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.
def main():
    """
    Main body function. Call all functions from here
    :return:
    """
    test_baseball_statistics()

if __name__ == "__main__":
    main()