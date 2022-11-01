#!/usr/bin/env python
# coding: utf-8

# Sol1) re module can be imported for generating Regex objects {re.compitle()}.

# Sol2) Raw strings often appear in regex objects to prevent backslash from escaping.

# Sol3) The return value of the search method is a match object if the object is present in the string else it returns none.

# Sol4) group() For matched items  group() method returns the actual string that match the pattern

# In[17]:


import re
match = re.search('ineuron','I am enrolled in a Data Science program with Ineuron', flags=re.IGNORECASE)
print('Output:',match.group())

Sol5) 
group zero covers the entire (\d\d\d)-(\d\d\d-\d\d\d\d)
group 1 covers (\d\d\d)
group 2 covers (\d\d\d-\d\d\d\d)Sol6) Periods and parentheses can be escaped with a backslash: \., \(, and \).Sol7) If there is a one group in the expression or regex pattern , findall() will return list of strings but if there is several groups in the expression, findall() returns list of tuple of strings.Sol8) In Standard Expressions | means either, OR operator.Sol10) In regex ' + ' refers one or more occurences
' * ' refers zero or more occurences.Sol11) {4} in regex means preceding character is to be repeated at least 4 times.
{4,5} in regex means preceding character is repeated at least 4 times and maximum 5 times or 4 to 5 times.Sol12) \d returns a match where the string contains digits from  0-9, \w returns a match where the string contains any word characters  from a to Z, digits from 0-9, and the underscore _ character, \s returns a match where the string contains a white space character
Sol 13) \D returns the match where the string doesn't have the digits, \W returns a match where the string doesn't contain any of the word characters, \S returns a match where the string doesn't contain a white space character.Sol14) .* is a Greedy mode, which returns the longest string when it meets the condition. Whereas .*? is a non greedy mode which returns the shortest string when it meets the condition.Sol15) The syntax for matching both numbers and lowercase letters with a character class is [a-z0-9].Sol16)  re.IGNORECASE is used as a flag to make a normal expression case insensitive.Sol 17) . character matches everything except newline character, if we passs re.DOTALL as a flag to re.compile(), we can make the dot character match all characters, including the newline character.Sol 18) 'X drummers, X pipers, five rings, X hen'.Sol19) re.VERBOSE it will allow to add whitespace and comments to string passed to re.compile().
# In[18]:


# Sol20)
re.compile(r'[A-Z][a-z]*\sNakamoto')


# In[ ]:




