#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector


# In[3]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="labor_force"
)


# In[4]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[5]:


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM labor_force")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[ ]:




