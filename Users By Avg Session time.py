#Question: Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. For simplicity, assume an user has only 1 
#session per day and if there are multiple of the same events in that day, consider only the latest page_load and earliest page_exit. Output the user_id and their average session
#time.

#link to Question: https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?python=1


# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log

facebook_web_log['day']=facebook_web_log['timestamp'].dt.day

page_load= facebook_web_log[facebook_web_log['action']=='page_load'].groupby(['user_id','day'])['timestamp'].max().reset_index()

page_exit= facebook_web_log[facebook_web_log['action']=='page_exit'].groupby(['user_id','day'])['timestamp'].min().reset_index()

merge = page_load.merge(page_exit, how='inner', on=['user_id','day'])

merge['session_time']= merge['timestamp_y'] - merge['timestamp_x']

merge.groupby('user_id')['session_time'].mean(numeric_only=False).reset_index()
