#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'

Expected Output :

No. of Upper case characters : 3

No. of Lower case Characters : 12


# In[1]:


def upplower():
    count_upper = 0
    count_lower = 0
    input_string = input('Enter the String : ')
    for char in input_string:
        if char.isupper():
            count_upper = count_upper + 1
        elif char.islower():
            count_lower = count_lower + 1
    print('Number of Upper Characters in the Entered Strings are : ' , count_upper)
    print('Number of Lower Characters in the Entered Strings are : ' , count_lower)
upplower()


# In[ ]:




