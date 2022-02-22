--Question:https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?python=

SELECT a.date,/*count(b.user_id_receiver),count(a.user_id_sender)*/
       count(b.user_id_receiver)/count(a.user_id_sender)::decimal AS percentage_acceptance
FROM
  (SELECT date, user_id_sender,
                user_id_receiver
   FROM fb_friend_requests
   WHERE action='sent' ) a
LEFT JOIN
  (SELECT date, user_id_sender,
                user_id_receiver
   FROM fb_friend_requests
   WHERE action='accepted' ) b ON a.user_id_sender=b.user_id_sender
AND a.user_id_receiver=b.user_id_receiver
GROUP BY a.date
