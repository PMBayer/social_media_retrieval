import praw
import json

reddit = praw.Reddit(client_id='xyIkPQ81K-QdDw',
                     client_secret='Y2-s7siZMj_4oNauP2Plnop3awI',
                     user_agent='first Bot',
                     username='Ikazoz',
                     password='Pasybayer123')


def get_data_from_reddit(subreddit, keyword):
    list_of_submissions = []
    sub_to_search = reddit.subreddit(subreddit)

    for submission in sub_to_search.search(keyword, limit=None):
        if submission.is_self:
            entry = {
                'user': submission.author.name,
                'upvote_ratio': submission.upvote_ratio,
                'title': submission.name,
                'post': submission.selftext,
                'url': submission.url,
            }
            list_of_submissions.append(entry)

    return list_of_submissions

