#Question: Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews.
#Order by total reviews in descending order.
#Link to Question:https://platform.stratascratch.com/coding/10049-reviews-of-categories?python=1


# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

df=yelp_business[['review_count', 'categories']].set_index('review_count').apply(lambda x: x.str.split(';').explode()).reset_index()

df1=df.groupby('categories')['review_count'].sum().reset_index().sort_values(by=['review_count'], ascending=False)

df1
