#!/usr/bin/env python
# coding: utf-8

# Author of exercise solutions: Genevieve LaLonde

# ___
# # Matplotlib Exercises 
# 
# Welcome to the exercises for reviewing matplotlib! 
# Take your time with these, Matplotlib can be tricky to understand at first. 
# These are relatively simple plots, but they can be hard if this is your first time with matplotlib, 
# feel free to reference the solutions as you go along.
# 
# Also don't worry if you find the matplotlib syntax frustrating, 
# we actually won't be using it that often throughout the course, 
# we will switch to using seaborn and pandas built-in visualization capabilities. 
# But, those are built-off of matplotlib, which is why it is still important to get exposure to it!
# 
# ** * NOTE: ALL THE COMMANDS FOR PLOTTING A FIGURE SHOULD ALL GO IN THE SAME CELL. 
# SEPARATING THEM OUT INTO MULTIPLE CELLS MAY CAUSE NOTHING TO SHOW UP. * **
# 
# # Exercises
# 
# Follow the instructions to recreate the plots using this data:
# 
# ## Data
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. 
# What command do you use if you aren't using the jupyter notebook?**
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exercise 1
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, y)
ax.set_xlabel('Amount of treats')
ax.set_ylabel('Amount my dog wags')
ax.set_title('Title')


# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])


# ** Now plot (x,y) on both axes. And call your figure object to show it.**
ax1.plot(x, y)
ax2.plot(x, y)
ax1.set_xlabel('Big X')
ax1.set_ylabel('Big Y')
ax2.set_xlabel('little x')
ax2.set_ylabel('little y')
ax1.set_title('Momma graph and baby graph')
fig


# ## Exercise 3
# 
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])


# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**
fig2 = plt.figure()

ax1 = fig2.add_axes([0,0,1,1])
ax2 = fig2.add_axes([0.2,0.5,.4,.4])

ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)


# ## Exercise 4
# 
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**
plt.subplot(1, 2, 1)
plt.subplot(1, 2, 2)


# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**
plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-.')
plt.subplot(1, 2, 2)
plt.plot(x, z, 'r--', lw=3)


# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.**
fig, axes = plt.subplots(1, 2, figsize=(12,2))

plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-.')

plt.subplot(1, 2, 2)
plt.plot(x, z, 'r--', lw=3)

