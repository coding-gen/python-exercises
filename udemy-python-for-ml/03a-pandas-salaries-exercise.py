#!/usr/bin/env python
# coding: utf-8

# Author of exercise solutions: Genevieve LaLonde

# ___
# # SF Salaries Exercise 
# Welcome to a quick exercise for you to practice your pandas skills! 
# We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! 
# Follow along and complete the tasks outlined in bold below. 
# The tasks will get harder and harder as you go along.
# ** Import pandas as pd.**

import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**
salaries = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **
salaries.head()


# ** Use the .info() method to find out how many entries there are.**
salaries.info()


# **What is the average BasePay ?**
salaries['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **
salaries['OvertimePay'].max()


# ** What is the job title of JOSEPH DRISCOLL?
salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **
salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**
salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].max()]


# ** What is the name of lowest paid person (including benefits)?**
salaries[salaries['TotalPayBenefits'] == salaries['TotalPayBenefits'].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
salaries.groupby('Year')['BasePay'].mean()


# ** How many unique job titles are there? **
salaries['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **
salaries['JobTitle'].value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? 
# (e.g. Job Titles with only one occurence in 2013?) **
salaries_2013 = salaries[salaries['Year']==2013]
title_counts_2013 = salaries_2013['JobTitle'].value_counts() 
unique_titles_2013 = title_counts_2013[title_counts_2013 == 1]
unique_titles_2013.count()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **
camel_counts = len(salaries[salaries['JobTitle'].str.contains('Chief')])
capital_counts = len(salaries[salaries['JobTitle'].str.contains('CHIEF')])
lower_counts = len(salaries[salaries['JobTitle'].str.contains('chief')])
all_counts = len(salaries[salaries['JobTitle'].apply(str.lower).str.contains('chief')])

print(f"Chief: {camel_counts}")
print(f"CHIEF: {capital_counts}")
print(f"chief: {lower_counts}")
print(f"all counts of Chief: {all_counts}")


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **
title_lengths = salaries['JobTitle'].apply(len)
correlation = pd.concat([salaries['TotalPayBenefits'], title_lengths],axis=1).corr()
correlation