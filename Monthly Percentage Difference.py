#Question: Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output should include the year-month date (YYYY-MM) and 
#percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year. The percentage change column will be populated 
#from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.

# Import your libraries
import pandas as pd
import datetime as dt

# Start writing code
sf_transactions.head()

sf_transactions['month']= sf_transactions['created_at'].dt.month
sf_transactions['year']= sf_transactions['created_at'].dt.year

#sf_transactions['year-month']= sf_transactions['created_at'].dt.year.astype('str')+ '-'+sf_transactions['created_at'].dt.month.astype('str')

sf_transactions=sf_transactions.groupby(['year','month'])['value'].sum().reset_index()

sf_transactions['pre']=sf_transactions['value'].shift(1)

sf_transactions['diff_percentage']=(sf_transactions['value']-sf_transactions['pre'])/sf_transactions['pre']*100

sf_transactions[['year', 'month', 'diff_percentage']]
sf_transactions
