#!/usr/bin/env python
# coding: utf-8

# ___
# # Python Crash Course Exercises 
# This is an optional exercise to test your understanding of Python Basics. 

# ## Exercises
# Answer the questions or complete the tasks outlined in bold below, 
# use the specific method described if applicable.

# ** What is 7 to the power of 4?**
7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **
s = "Hi there Sam!"
s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.
planet = "Earth"
diameter = 12742
print(f"The diameter of {planet} is {diameter} kilometers.")


# ** Given this nested list, use indexing to grab the word "hello" **
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
def domainGet(s):
    return s[s.find('@') + 1:]
 

print(domainGet('user@domain.com'))


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. 
# Don't worry about edge cases like a punctuation being attached to the word dog, 
# but do account for capitalization. 
def findDog(s):
    if s.find('dog') > 0:
        return True
    return False
    
findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. 
# Again ignore edge cases. 
import re
def countDog(s):
    regex = 'dog'             
    return len(re.findall(regex, s))


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list
# that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']
seq = ['soup','dog','salad','cat','great']
first_s = lambda a : a[0] == 's'

[t for t in filter(first_s, seq)]


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. 
# Write a function to return one of 3 possible results: 
# "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". 
# If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
# If speed is 81 or more, the result is "Big Ticket". 
# Unless it is your birthday (encoded as a boolean value in the parameters of the function).
# on your birthday, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 'No Ticket'
    elif speed <= 80:
        return 'Small Ticket'
    return 'Big Ticket'

caught_speeding(81,True)
caught_speeding(81,False)