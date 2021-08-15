#Question: Find the titles of workers that earn the highest salaries. Output the highest-paid titles.
#Link to Question: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?python=1

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

max_salary=worker[worker['salary']==worker['salary'].max()]

df=max_salary.merge(title, how='inner', left_on='worker_id', right_on='worker_ref_id')

df['worker_title']
