#Question: Find the employee with the highest salary per department.
#Output the department name, employee's first name along with the corresponding salary.
#Link : https://platform.stratascratch.com/coding/9897-highest-salary-in-department?python=1


# Import your libraries
import pandas as pd

# Start writing code
employee

df=employee.groupby(['department'])['salary'].max().reset_index().sort_values(by=['salary'], ascending=False)

result = employee.merge(df, on=['department','salary'], how='inner')
result[['department','first_name','salary']]
