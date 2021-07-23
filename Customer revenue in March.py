# Import your libraries
import pandas as pd

# Start writing code
orders.head()

order_march= orders[(pd.DatetimeIndex(orders['order_date']).month==3) & (pd.DatetimeIndex(orders['order_date']).year==2019)]

order_march['revenue']= order_march['order_quantity']*order_march['order_cost']

order_march.groupby('cust_id')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
