#Question:Find the customer with the highest total order cost within a single day between 2019-02-01 to 2019-05-01. Total order cost is calculated as order_cost*order_quantity. 
#Output their first name, total cost of their items, and the date.For simplicity, you can assume that every first name in the dataset is unique. 
#Also, the cost of the certain item (e.g. coat) could vary among different purchases (not all coats cost the same).
#Link : https://platform.stratascratch.com/coding/9915-highest-cost-orders?python=1

# Import your libraries
import pandas as pd

# Start writing code
customers.head()

df=customers.merge(orders, how='inner', left_on='id', right_on='cust_id')

df['Cost']=df['order_quantity']*df['order_cost']
df.head()
df1=df[df['order_date'].between('2019-02-1', '2019-05-1')]
df2=df1.groupby(['first_name', 'order_date'])['Cost'].sum().reset_index()
df2.head()
ans=df2[df2['Cost']==df2["Cost"].max()]
ans['order_date'] = pd.to_datetime(ans['order_date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
ans
