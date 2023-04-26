#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[3]:


salaries = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[4]:


salaries.head()


# ** Use the .info() method to find out how many entries there are.**

# In[5]:


salaries.info()


# **What is the average BasePay ?**

# In[9]:


salaries['BasePay'].mean()


# In[10]:





# ** What is the highest amount of OvertimePay in the dataset ? **

# In[10]:


salaries['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[18]:


salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# In[12]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[19]:


salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[13]:





# ** What is the name of highest paid person (including benefits)?**

# In[25]:


salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].max()]


# In[14]:





# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[26]:


salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()]


# In[15]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[31]:


salaries.groupby('Year')['BasePay'].mean()


# In[16]:





# ** How many unique job titles are there? **

# In[37]:


salaries['JobTitle'].nunique()


# In[17]:





# ** What are the top 5 most common jobs? **

# In[38]:


salaries['JobTitle'].value_counts().head()


# In[18]:





# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[89]:


salaries_2013 = salaries[salaries['Year']==2013]
title_counts_2013 = salaries_2013['JobTitle'].value_counts() 
unique_titles_2013 = title_counts_2013[title_counts_2013 == 1]
unique_titles_2013.count()


# In[19]:





# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[137]:


camel_counts = len(salaries[salaries['JobTitle'].str.contains('Chief')])
capital_counts = len(salaries[salaries['JobTitle'].str.contains('CHIEF')])
lower_counts = len(salaries[salaries['JobTitle'].str.contains('chief')])
all_counts = len(salaries[salaries['JobTitle'].apply(str.lower).str.contains('chief')])

print(f"Chief: {camel_counts}")
print(f"CHIEF: {capital_counts}")
print(f"chief: {lower_counts}")
print(f"all counts of Chief: {all_counts}")


# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[149]:


title_lengths = salaries['JobTitle'].apply(len)
correlation = pd.concat([salaries['TotalPayBenefits'], title_lengths],axis=1).corr()
correlation


# In[23]:





# # Great Job!
