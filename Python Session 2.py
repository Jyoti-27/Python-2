#!/usr/bin/env python
# coding: utf-8

# In[3]:


name = "Jyoti"
age = 35
print(name)
print(age)


# In[6]:


print("Jyoti")
print(name,age)


# In[8]:


print("My name is ",name)


# In[16]:


Course = "PCDS"
Cohort = "August"
print("My Course is", Course)
print("I belong the Cohort of", Cohort)


# In[1]:


name = "Jyoti"
age = 35
type(name)
type(age)


# In[2]:


name = "Jyoti"
age = 35
height = 156.5
weight = 45


# ## Data Types in Python

# - Some data types are mutable and some are immutable
# - Mutable are ones which can be modified
# - Immutable are the ones that can be modified once you create them

# Below given are the few data types that we have in Python
# - Numeric
# - String
# - Tuples
# - List
# - Dictionaries
# - Set
# - None 
# - Range
# 

# Mutable data types in Python
# - List
# - Dictionaries
# - Set

# Immutable data types in Python
# - Numeric
# - String
# - Tuples

# - Let's start our discussion with the immutable data types in Python
# - We will start our discussion with Numeric data typesin Python

# ### Numeric Data Types in Python
# In Python we have 4 Numeric data types
# - Integer
# - Float
# - Boolean
# - Complex
# 

# Let's talk about the Ineger data types in Python

# In[9]:


# Create two Variables a and b with some integer values assigned to them
a = 25
b = 2
type(a)


# In[15]:


# Let's perform some Arithmetic Operations on the Integer data types
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Float Division
print(a // b) # Truncated Division
print(a ** b) # Exponential Operator


# Create two variables x and y with integer values.Then perform float division , truncated division and exponent(find x rise to power)

# In[17]:


x = 9
y = 2
print(x / y)
print(x // y)
print(x ** y)


# In[19]:


### Float data type in Python
A = 2.56
B = 3.57
type(A)


# In[24]:


a = 12.9
b = 3.6
c = a + b # Addition
d = a - b # Sutraction
e = a * b # Watch out for the roud off error! # Multiplication
f = a / b # Float Division
print(a, b, c, d, e, f, sep="\n")
print(a, b, c, d, e, f)


# In[25]:


a = 12.5
print(type(a))


# In[ ]:




