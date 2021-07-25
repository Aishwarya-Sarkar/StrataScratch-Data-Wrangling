# Import your libraries
import pandas as pd

# Start writing code
customers.head()

df=customers.merge(orders, how= 'inner', right_on='cust_id' , left_on='id')

df1=df.groupby('cust_id')['order_quantity'].count().reset_index()

df1[df1['order_quantity']== df1['order_quantity'].max()][['cust_id', 'order_quantity']]
