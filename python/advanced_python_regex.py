PLACE YOUR CODE HERE

import csv
import re

### TO DETERMINE FREQUENCY OF DEGREES
with open('faculty.csv', 'r') as facultylist:
    new_cont = {}
    def addToList(str_to_add):
        if str_to_add not in new_cont:
            new_cont[str_to_add] = 1
        else:
            new_cont[str_to_add] += 1
    reader = csv.reader(facultylist, delimiter="\t")
    container = []
    for row in reader:
        container.append(row[0].replace('.','').split(',')[1].split(' '))
    # print(container)
    for element in container:
        for item in element:
            addToList(item)
    if '' in new_cont: del new_cont['']
    if 'degree' in new_cont: del new_cont['degree']
    if '0' in new_cont: del new_cont['0']
    print (new_cont)

### TO DETERMINE FREQUENCY OF TITLES

with open('faculty.csv', 'r') as facultylist:
     new_cont = {}
     def addToList(str_to_add):
         if str_to_add not in new_cont:
             new_cont[str_to_add] = 1
         else:
             new_cont[str_to_add] += 1
     reader = csv.reader(facultylist, delimiter="\t")
     container = []
     for row in reader:
         container.append(row[0].split(','))
     for element in container:
         a = element[2]
         regex = r'(.*Professor)'
         matches = re.findall(regex, a)
         for match in matches:
             addToList(match)
     print(new_cont)

## TO GATHER LIST OF EMAIL ADDRESSES

with open('faculty.csv', 'r') as facultylist:
      new_cont = []
      reader = csv.reader(facultylist, delimiter="\t")
      container = []
      for row in reader:
          container.append(row[0].split(','))
      for element in container:
          a = element[3]
          regex = r'.*@.*'
          matches = re.findall(regex, a)
          for match in matches:
              new_cont.append(match)
      print(new_cont)

## TO DETERMINE FREQUENCY OF DOMAIN NAMES

with open('faculty.csv', 'r') as facultylist:
      new_cont = {}
      def addToList(str_to_add):
          if str_to_add not in new_cont:
              new_cont[str_to_add] = 1
          else:
              new_cont[str_to_add] += 1
      reader = csv.reader(facultylist, delimiter="\t")
      container = []
      for row in reader:
          container.append(row[0].split(','))
      for element in container:
          a = element[3]
          regex = r'@.*'
          matches = re.findall(regex, a)
          for match in matches:
              addToList(match[1:])
      print(new_cont)



