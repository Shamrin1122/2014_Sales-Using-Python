#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_excel("Sales_2014.xlsx", sheet_name="sales_2014")
df


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[14]:


for i in df.select_dtypes(include="object"). columns:
    print (df[i].value_counts())
    print("__"*10)


# In[17]:


df.duplicated().sum()


# In[18]:


df.describe().T


# In[21]:


df['month_number'] = df['Order Date'].dt.month
df['month_name'] = df['Order Date'].dt.month_name()
df


# In[41]:


plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='month_name', y='Order Quantity')
plt.title("Month Wise Order Quantity")
plt.xlabel("month_name")
plt.ylabel("Order Quantity")
plt.tight_layout()
plt.show()


# In[59]:


df.groupby('Order Priority')['Order Quantity'].sum().plot.pie(
    autopct='%1.1f%%',
    figsize=(8, 8),
    startangle=90   
)
plt.title("Quantity Wise Order Priority")
plt.show()


# In[49]:


plt.figure(figsize=(5, 6))
sns.barplot(data=df, x='SalesPerson', y='Final Price')
plt.title("Top Sales Person")
plt.xlabel("Sales Person")
plt.ylabel("Price")
plt.tight_layout()
plt.show()


# In[57]:


plt.figure(figsize=(12, 5))
sns.lineplot(x='month_name', y='Final Price', data=df)
plt.title("Month Wise Sales")
plt.show()


# In[74]:


top_sku = df.groupby('SKU')['Final Price'].sum().sort_values(ascending=False).head(5)
top_sku.plot(kind='bar', figsize=(8, 5), color='lightblue')

plt.title('Top SKU Final Price Wise(After Discount)')
plt.xlabel('SKU')
plt.ylabel('Final Price')

plt.show()


# In[70]:


plt.figure(figsize=(5, 6))
sns.barplot(data=df, x='Ship Mode', y='Shipping Amount')
plt.title("Shipping Amount Vs Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Shipping Amount")
plt.tight_layout()
plt.show()


# In[75]:


top_cust = df.groupby('Customer ID')['Order Quantity'].sum().sort_values(ascending=False).head(5)
top_cust.plot(kind='bar', figsize=(8, 5), color='lightblue')

plt.title('Top Customers Order Quantity Wise')
plt.xlabel('Customer')
plt.ylabel('Quantity')

plt.show()


# In[ ]:




