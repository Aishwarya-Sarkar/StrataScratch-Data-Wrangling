#Question: Classify each business as either a restaurant, cafe, school, or other. A restaurant should have the word 'restaurant' in the business name.
#For cafes, either 'cafe' or 'coffee' can be in the business name. 'School' should be in the business name for schools. All other businesses should be classified as 'other
#Link to question: https://platform.stratascratch.com/coding/9726-classify-business-type?python=1

# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()
df=sf_restaurant_health_violations

def classify(businessName):
    if ('SCHOOL' in businessName):
        return 'school'
    elif ('CAFE' in businessName) or ('COFFEE' in businessName):
        return 'cafe'
    elif ('RESTAURANT' in businessName):
        return 'restaurant'
    else:
        return 'other'
    
df['business_type']= df.apply(lambda x: classify(x['business_name'].upper()), axis=1)
df[['business_name','business_type']].drop_duplicates()
