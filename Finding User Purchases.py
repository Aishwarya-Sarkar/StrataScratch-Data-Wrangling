#Write a query that'll identify returning active users. 
#A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users
#Link to Qs: https://platform.stratascratch.com/coding/10322-finding-user-purchases?python=1

# Import your libraries
import pandas as pd

# Start writing code
amazon_transactions.head(20)
df=amazon_transactions.sort_values(by=['user_id','created_at'], ascending=[True, True])
df['pre']=df.groupby('user_id')['created_at'].shift(1)
df['diff']=(df['created_at']-df['pre']).dt.days
df[(df['diff']<=7) & (df['diff']>=0)]['user_id'].unique()
