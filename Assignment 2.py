#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Give 20 methods of list, tuples and dictionaries with examples


# In[2]:


#List

#1.append()
#Adds an element to the end of the list.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  


# In[3]:


#2.insert()
#Inserts an element at a specific index.

my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  


# In[16]:


#3.extend()
#Extends the list by appending elements from an iterable.

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)


# In[4]:


#4.remove()
#Removes the first occurrence of a value.

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  


# In[5]:


#5.pop()
#Removes and returns an element at a specific index.

my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(my_list, popped_element)


# In[17]:


#6.reverse()
#Reverses the elements of the list in-place.

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)


# In[18]:


#7.sort()
#Sorts the elements of the list in-place.

my_list = [3, 1, 2]
my_list.sort()
print(my_list)


# In[19]:


#8.copy()
#Returns a shallow copy of the list.

my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list) 


# In[ ]:





# In[6]:


#Tuples:

#1.count()
#Returns the number of occurrences of a value in the tuple.

my_t = (1, 2, 2, 3)
count = my_t.count(2)
print(count)


# In[7]:


#2.index()
#Returns the index of the first occurrence of a value.

my_t = (1, 2, 3, 2)
index = my_t.index(2)
print(index) 


# In[ ]:





# In[8]:


#Dictionaries:

#1.get()
#Returns the value for a given key, or a default value if the key is not present.

my_dict = {'a': 1, 'b': 2}
tracy = my_dict.get('a', 0)
print(tracy)


# In[9]:


#2.keys()
#Returns a view of all keys in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys) 


# In[10]:


#3.values()
#Returns a view of all values in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)


# In[11]:


#4.items()
#Returns a view of all key-value pairs in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items) 


# In[12]:


#5.pop()
#Removes and returns the value for a given key.

my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(my_dict, value) 


# In[13]:


#6. popitem()
#Removes and returns a key-value pair as a tuple.

my_dict = {'a': 5, 'b': 6, 'c': 7}
item = my_dict.popitem()
print(my_dict, item)


# In[14]:


#7.update()
#Updates the dictionary with elements from another dictionary or iterable.

my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)


# In[15]:


#8.clear()
#Removes all items from the dictionary.

my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)


# In[ ]:




