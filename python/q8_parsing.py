# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import collections


with open('football.csv', 'r') as football_list:
    reader = csv.reader(football_list, delimiter="\t")
    next(reader, None)  # skip the headers
    container1 = []
    container2 = {}
    for row in reader:
        container1.append(row[0].split(','))
    for element in container1:
      team_name = element[0]
      team_goals = int(element[5]) - int(element[6])
      container2[team_name] = team_goals
    diff = float('inf')
    for key,value in container2.items():
        if diff > abs(0-value):
            diff = abs(0-value)
            x = key
    print(x)


## Answer is Aston Villa
