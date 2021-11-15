#!/usr/bin/env python
# coding: utf-8

# TASK 3 : Exploratory Data Analysis-Retail. Perform 'Explanatory Data Analysis' on dataset 'SampleSuperstore'.
# 
# DATASET : https://bit.ly/3i4rbWl
# 
# EXAMPLE QUESTION : As a business manager, try to findout the weak areas where you can work to make more profit. What all business problems you can derive by exploring the data?
# 
# LEVEL : Beginner
# 
# NAME OF THE AUTHOR : Gokul Raj, Data Science and Business Analytics Intern, The Sparks Foundation.
# 

# In[47]:


#importing necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[48]:


import warnings
warnings.filterwarnings('ignore')


# In[49]:


sns.color_palette("tab10")


# In[50]:


data=pd.read_csv("SampleSuperstore.csv")


# In[51]:


#Loading first 5 rows
data.head()


# In[52]:


#Loading lat 5 rows
data.tail()


# In[53]:


data.shape


# In[54]:


#Loading Statistical overview of the data
data.describe()


# In[55]:


#Loading columns inside the dataset
data.columns


# In[56]:


#Loading overall information about data
data.info()


# In[57]:


data['Country'].value_counts()


# In[59]:


#Calculating the cost
data['Cost']=data['Sales']-data['Profit']

#Calculating Profit Percentage
data['Profit%']=(data['Profit']/data['Cost'])*100


# In[60]:


data.head()


# MULTIVARIATE VISUALIZATIONS

# In[61]:


#Correlation matrix and heatmap
datacorr=data.corr()
sns.heatmap(datacorr, annot=True, cmap='RdYlGn')
plt.title('Correlation between the variables')


# FINDING THE MODES OF SHIPPING PRODUCTS AND OBSERVING WHICH IS MORE PREFERRED MODE OF SHIPPING?

# In[62]:


shipmodetypes=data.groupby('Ship Mode')
for i,df in shipmodetypes:
    print(i)


# In[63]:


data.groupby('Ship Mode').groups


# In[64]:


data['Ship Mode'].value_counts()


# In[65]:


sns.histplot(x=data['Ship Mode'], color='g')
plt.title('Ship Mode Preference')


# CUSTOMER SEGMENTS
# 

# In[66]:


segmenttypes=data.groupby('Segment')
for i,df in segmenttypes:
    print(i)


# In[67]:


data['Segment'].value_counts()


# In[68]:


sns.histplot(x=data['Segment'])
plt.title('Customer Segments')


# CATEGORY-WISE ANALYSIS
# 

# In[69]:


cat=data.groupby('Category')
for i,df in cat:
    print(i)


# In[70]:


sns.countplot(x=data['Category'])
plt.title('Categories of Products')


# In[71]:


sns.countplot(x=data['Region'], hue=data['Category'])
plt.title('Region-wise Ordered Product Categories')


# In[72]:


sns.scatterplot(x=data['Ship Mode'], y=data['Sales'], hue=data['Category'])


# In[73]:


ds=data.groupby('Category')['Profit', 'Sales'].agg('sum')
print(ds)
ds.plot.bar()
plt.legend(loc='upper left')
plt.title('Category-wise Profit and Sale')


# SUB-CATEGORY-WISE-ANALYSIS

# In[75]:


subcatarr=[]
subcat=data.groupby('Sub-Category')
for i,df in subcat:
    print(i)
    subcatarr.append(i)


# In[76]:


plt.figure(figsize=(10,10))
data['Sub-Category'].value_counts().plot.pie(autopct="%1.1f%%")
plt.title('Quantity of different Sub-Categories Ordered')


# REGION-WISE ANALYSIS

# In[78]:


regions=data.groupby('Region')
for i,df in regions:
    print(i)


# In[79]:


rw=data.groupby('Region')['Profit', 'Sales'].agg('sum')
rw.plot.bar()
plt.legend(loc='upper left')
plt.title('Region-wise Profit and Sales')


# In[80]:


plt.figure(figsize=(10,10))
data['Region'].value_counts().plot.pie(autopct="%1.1f%%")


# CITY-WISE ANALYSIS

# In[81]:


city=[]
cities=data.groupby('City')
for i,df in cities:
    city.append(i)


# In[82]:


city


# In[83]:


len(city)


# In[84]:


data['City'].value_counts()


# In[85]:


data['City'].value_counts().min()


# In[86]:


data['City'].value_counts().max()


# In[87]:


data[data['City']=='New York City']

