# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary

#3. DENSE_RANK() --> RANK(method='dense')
ms_employee_salary['DenseRank'] = ms_employee_salary.groupby(['first_name', 'last_name', 'department_id'])['salary'].rank(method='dense', ascending= False)

ms_employee_salary[ms_employee_salary['DenseRank']==1][['id', 'first_name', 'last_name', 'department_id', 'salary']]
