''' Question: What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. 
Order by the earliest date to latest.

Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) that's logged in the table with 
action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

Link: https://platform.stratascratch.com/coding-question?id=10285&python=1'''


# Import your libraries
import pandas as pd

# Start writing code
fb_friend_requests.head(10)

sent_req = fb_friend_requests[fb_friend_requests['action'] == 'sent']
accepted_req = fb_friend_requests[fb_friend_requests['action'] == 'accepted']
cmbd = pd.merge(sent_req, accepted_req, how = 'left', left_on = ['user_id_sender', 'user_id_receiver'], right_on = ['user_id_sender', 'user_id_receiver'])

dates = cmbd.groupby('date_x').count().reset_index()
dates['acceptance_rate'] = dates['action_y']/dates['action_x']
dates
result = dates[['date_x', 'acceptance_rate']]
