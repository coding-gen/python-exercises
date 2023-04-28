#!/usr/bin/env python
# coding: utf-8

# Author of exercise solutions: Genevieve LaLonde

# ___
# # Ecommerce Purchases Exercise
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! 
# Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. 
# Feel free to reference the solutions. Most of the tasks can be solved in different ways. 
# For the most part, the questions get progressively harder.
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# Also note that all of these questions can be answered with one line of code.
# ____


# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **
import pandas as pd
purchases = pd.read_csv('Ecommerce Purchases')


# **Check the head of the DataFrame.**
purchases.head()


# ** How many rows and columns are there? **
purchases.info()


# ** What is the average Purchase Price? **
purchases['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **
purchases['Purchase Price'].max()
purchases['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **
sum(purchases['Language'] == 'en')


# ** How many people have the job title of "Lawyer" ? **
(purchases['Job'] == 'Lawyer').value_counts()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
purchases['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **
purchases['Job'].value_counts().head()


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **
purchases[purchases['Lot'] == "90 WT"]['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **
purchases[purchases['Credit Card'] == 4926535242672853]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# As a cheat, I count how many entries are in just one column.
# I've selected one of the columns we already filtered on, in case that can be handled by and merged in by the optimizer.
purchases[(purchases['CC Provider'] == 'American Express') & (purchases['Purchase Price'] > 95)]['Purchase Price'].count()


# ** Hard: How many people have a credit card that expires in 2025? **
sum(purchases['CC Exp Date'].str.slice(3,) == '25')


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **
purchases['Email'].str.rsplit('@', expand=True)[1].value_counts().head()
