#Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the difference in salaries.
#Link to question: https://platform.stratascratch.com/coding/10308-salaries-differences?python=1

# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
db_dept.head(20)

df=db_dept[db_dept['department'].isin(['engineering','marketing'])]

df = db_employee.merge( db_dept, how = 'inner',left_on = ['department_id'], right_on=['id'])

df1=df[df["department"]=='engineering']
eng = df1.groupby('department')['salary'].max().reset_index()

df2=df[df["department"]=='marketing']
marketing = df2.groupby('department')['salary'].max().reset_index()

result = pd.DataFrame(abs(eng['salary'] - marketing['salary']))
result

