from collections import OrderedDict

famous_people_dict = { 'Clinton': [['JD', 'Politician','Arkansas'], ['High School', 'Musician','North Carolina']],
              'Kennedy': [['JD', 'Politician', 'Massachusetts'], ['BA','Writer','New York']],
              'Kerr' :['BA','Athlete','Lebanon']
              }

for key in sorted(famous_people_dict)[:3]:
    print (key, famous_people_dict[key])

famous_people_dict_two = {('Bill', 'Wine'): ['JD', 'Politician', 'Arkansas'], ('George', 'Clinton'): ['High School', 'Musician', 'North Carolina'], ('John', 'Kennedy'): ['JD', 'Politician', 'Massachusetts'], ('William','Kennedy'): ['BA', 'Writer', 'New York'], ('Steve','Kerr'): ['BA', 'Athlete', 'Lebanon'] }

for key in sorted(famous_people_dict_two)[:3]:
    print (key, famous_people_dict_two[key])

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

    ## TO SORT BY LAST NAME
print(OrderedDict(sorted(professor_dict.items(), key=lambda name: name[0][1])))

Ellenberg Susan ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
Ellenberg Jonas ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
Li Yimei ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
Li Mingyao ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
Li Hongzhe ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']

