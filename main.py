from retrieve_reddit_data import get_data_from_reddit

subreddit = input('Please enter the subreddit you want to search!')
keyword = input('Please enter the word you want to search reddit for!')

submissions = get_data_from_reddit(subreddit, keyword)

