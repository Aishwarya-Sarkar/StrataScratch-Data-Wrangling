#Question :Find the date with the highest total energy consumption from the Facebook data centers. Output the date along with the total energy consumption across all data centers.
#Link : https://platform.stratascratch.com/coding-question?id=10064&python=1


# Import your libraries
import pandas as pd

# Start writing code
fb_eu_energy.head()

#concat all three dataframes
union= pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])
union.head()
union= union.groupby('date').sum().reset_index()

union[union['consumption']==union['consumption'].max()][['date', 'consumption']]
