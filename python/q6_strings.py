xsx# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        print('Number of donuts: many')
    else:
        print('Number of donuts: ', count)



    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    # raise NotImplementedError


def both_ends(s):
    if len(s) < 2:
        print ("")
    else:
        first_two = s[:2]
        last_two = s[-2:]
        print(first_two + last_two)

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    # raise NotImplementedError


def fix_start(s):
    special_char = s[0]
    b = s[1:]
    c = b.replace(special_char,'*')
    print (special_char+c)

    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    # raise NotImplementedError


def mix_up(a, b):
    first_chars_first_word = a[:2]
    first_chars_second_word = b[:2]
    remaining_first_word = a[2:]
    remaining_second_word = b[2:]
    print(first_chars_second_word+remaining_first_word, first_chars_first_word+remaining_second_word)


    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    # raise NotImplementedError


def verbing(s):
    if len(s) < 3:
        print (s)
    elif s[-3:] == 'ing':
        print (s+'ly')
    else:
        print(s+'ing')


    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    # raise NotImplementedError


def not_bad(s):
    not_str_index = s.find('not')
    bad_str_index = s.find('bad')
    first_part = s[:not_str_index]
    second_part = s[(bad_str_index+3):]
    if bad_str_index > not_str_index:
        print(first_part+'good'+second_part)
    else:
        print(s)



    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    # raise NotImplementedError

import math

def front_back(a, b):
    first_set = []
    second_set = []
    def even(word):
        even_val = int(len(word) / 2)
        first_set.append((word[:even_val]))
        second_set.append((word[even_val:]))
    def odd(word):
        odd_val = int(math.ceil(len(a) / 2))
        first_set.append((word[:(odd_val)]))
        second_set.append((word[odd_val:]))
    array = [a,b]
    for i in array:
        if len(i) % 2 == 0:
            even(i)
        if len(i) % 2 != 0:
            odd(i)
    print (first_set[0]+first_set[1]+second_set[0]+second_set[1])




    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    # raise NotImplementedError
