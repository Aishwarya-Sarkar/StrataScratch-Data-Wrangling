#Link to Question: https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?python=1
#Question: You're given a dataset of health inspections. Count the number of inspections that resulted in a violation for 'Roxanne Cafe' for each year.
#If an inspection resulted in a violation, there will be a value in the 'violation_id' column. Output the number of inspections by year in ascending order.

# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations

df=sf_restaurant_health_violations[sf_restaurant_health_violations['business_name']=='Roxanne Cafe']
df['year']=df['inspection_date'].dt.year

df.groupby('year')['violation_id'].count().reset_index().sort_values('violation_id', ascending=True)
