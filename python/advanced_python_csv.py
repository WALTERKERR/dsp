### TO BUILD CSV FILE BASED ON EMAIL ADDRESSES
import csv
import re

new_cont = []

with open('faculty.csv', 'r') as facultylist:
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



with open('email_list.csv', 'w') as csvfile:
    # fieldnames = ['Record number','email address']
    fieldnames = ['email address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    counter = 0
    while counter <= len(new_cont):
        for item in new_cont:
            counter += 1
            # writer.writerow({'Record number': counter, 'email address': item})
            writer.writerow({'email address': item})
