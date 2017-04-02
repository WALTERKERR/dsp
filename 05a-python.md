# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A list is mutable a tuple is not.  As a result, you can access the key in a list, but not in a tuple.  In a tuple, order matters, so the the index number (as opposed to its name) of an item is important .  In a list, you can use different data types.  I found this good stackoverflow answer to the list v. tuple discussion:
```
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.

You can't add elements to a tuple. Tuples have no append or extend method.
You can't remove elements from a tuple. Tuples have no remove or pop method.
You can find elements in a tuple, since this doesn’t change the tuple.
You can also use the in operator to check if an element exists in the tuple.
Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a list is like having an implied assert statement that this data is constant, and that special thought (and a specific function) is required to override that.
Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.
```

```
someTuple = (1,2)
someList  = [1,2]
```

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Big differences.  Sets have keys and cannot have duplicate keys.  They are also unordered.  Lists are ordered and can include duplicates.  If you want to be able to sort and have order, go with a list. If you favor accessing via keys and don't care about order, go with a set.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>> A lambda is a one-time function, designed for the immediate need and not to be referred to again. For example, using the dictionary below:
```python
famous_people_dict_two = {('Bill', 'Clinton'): ['JD', 'Politician', 'Arkansas'], ('George', 'Clinton'): ['High School', 'Musician', 'North Carolina'], ('John', 'Kennedy'): ['JD', 'Politician', 'Massachusetts'], ('William','Kennedy'): ['BA', 'Writer', 'New York'], ('Steve','Kerr'): ['BA', 'Athlete', 'Lebanon'] }
```

>>> we can use the following lambda function to sort:
```python
import collections
print(collections.OrderedDict(sorted(famous_people_dict_two.items(), ke
    ...: y=lambda name: name[0][1])))

```
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow sequences to be built on top of other sequences.  For example, with filter, you can apply a conditional statement to evaluate a series/sequence and then only deal with those values that meet the condition.  With map, you can manipulate items in the sequence themselves.  So, working together, if you had a sequence [1,2,3,4,5,6], you could use filter to choose only even integers within the sequence, and then map to manipulate those selected even values to square them, resulting in a sequence that would look like [4, 16, 36].  With regards to the difference between a set and a dictionary, these bullets from stackexchange provide a good,quick synopsis:
```
Do you just need to know whether or not you've already got a particular value, but without ordering (and you don't need to store duplicates)? Use a set.
Do you need to associate values with keys, so you can look them up efficiently (by key) later on? Use a dictionary.
```
Example using map:
```python
In [31]: sequence = [1, 2, 3, 4, 5]
    ...: cubed = list(map(lambda x: x**3, sequence))
    ...: print(cubed)
    ...: 
    ...: 
[1, 8, 27, 64, 125]
## This will cube every function within the sequence and produce a new array.
```
Example using filter:
```python
In [36]: sequence = [1,2,3,4,5]
    ...: evens  = list(filter(lambda x: not x % 2, sequence))
    ...: print(evens)
```


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





