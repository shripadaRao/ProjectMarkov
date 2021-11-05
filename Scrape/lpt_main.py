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

hot_subreddit = subreddit.top('all')

for post in hot_subreddit:
    post_dict = {
        "title" : [],
    }

    for post_title in hot_subreddit:
        
        if not post_title.stickied:
            post_dict["title"].append(post_title.title)
            

#print(post_dict)

    post_data = pd.DataFrame(post_dict)

    post_data.to_csv('main_raw.csv')

#3470 words 19363 characters


   