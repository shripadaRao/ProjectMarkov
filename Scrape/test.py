import praw 

import praw

import pandas as pd

reddit = praw.Reddit(
    client_id = 'acgZyikQDiF-FJU0_WNhtg',
    client_secret = 'sxQyN0ipycbtvb-XGDp6DhRz1nHgWA',
    username = 'Reddit_scrape_test',
    password = 'Holiday@social',
    user_agent = 'praw_tut',
)


subreddit = reddit.subreddit('LifeProTips')

hot_subreddit = subreddit.hot(limit = 10)

for post_title in hot_subreddit:
    if not post_title.stickied:
        print(post_title.title)

    #post_data = pd.DataFrame(post_title)


