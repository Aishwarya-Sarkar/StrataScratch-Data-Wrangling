# Import your libraries
import pandas as pd

# Start writing code
customers.head()

df=customers.merge(orders, how= 'inner', right_on='cust_id' , left_on='id')

df['total_orders']= df.groupby('cust_id')['order_quantity'].sum()

df[df['total_orders']== df['total_orders'].max()][['cust_id', 'total_orders']]
