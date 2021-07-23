#Question: Calculate the total revenue from each customer in March 2019. Revenue for each order is calculated by multiplying the order_quantity with the order_cost.
#Output the revenue along with the customer id and sort the results based on the revenue in descending order.
#Link to Question: https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?python=1


# Import your libraries
import pandas as pd

# Start writing code
orders.head()

order_march= orders[(pd.DatetimeIndex(orders['order_date']).month==3) & (pd.DatetimeIndex(orders['order_date']).year==2019)]

order_march['revenue']= order_march['order_quantity']*order_march['order_cost']

order_march.groupby('cust_id')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
