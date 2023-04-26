#!/usr/bin/env python
# coding: utf-8

# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. 
# We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.


import numpy as np


# #### Create an array of 10 zeros 
np.zeros(10)


# #### Create an array of 10 ones
np.ones(10)


# #### Create an array of 10 fives
np.ones(10)*5


# #### Create an array of the integers from 10 to 50
np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50
np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8
np.arange(0,9).reshape(3,3)


# #### Create a 3x3 identity matrix
np.identity(3)


# #### Use NumPy to generate a random number between 0 and 1
np.random.random()


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.normal(size=25)


# #### Create the following matrix:
np.arange(0.01, 1.01, 0.01)


# #### Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
m = np.arange(1,26).reshape(5,5)
m[2:,1:]

m[3,4]

m[:3,1].reshape(3,1)

m[4]

m[3:]


# ### Now do the following
# #### Get the sum of all the values in mat
m.sum()


# #### Get the standard deviation of the values in mat
m.std()


# #### Get the sum of all the columns in mat
m.sum(axis = 0)
