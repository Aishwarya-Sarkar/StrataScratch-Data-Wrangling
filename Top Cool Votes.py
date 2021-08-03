#Question: Find the business and the review_text that received the highest number of  'cool' votes.Output the business name along with the review text.
#Link to Question: https://platform.stratascratch.com/coding/10060-top-cool-votes?python=1

# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()

yelp_reviews[yelp_reviews['cool']==yelp_reviews['cool'].max()][['business_name','review_text']]
