'''Finding Updated Records
We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. 
Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary.
Order your list by employee ID in ascending order.

Link to question : https://platform.stratascratch.com/coding-question?id=10299&python=1
'''


# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary

#3. DENSE_RANK() --> RANK(method='dense')
ms_employee_salary['DenseRank'] = ms_employee_salary.groupby(['first_name', 'last_name', 'department_id'])['salary'].rank(method='dense', ascending= False)

ms_employee_salary[ms_employee_salary['DenseRank']==1][['id', 'first_name', 'last_name', 'department_id', 'salary']]
