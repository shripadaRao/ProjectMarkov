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

for post in hot_subreddit:
    post_dict = {
        "title" : [],
        "id" : [],
        "score" : [],
    }

    for post_title in hot_subreddit:
        
        if not post_title.stickied:
            post_dict["title"].append(post_title.title)
            post_dict["id"].append(post_title.id)
            post_dict["score"].append(post_title.score)
            


#print(post_dict)

    post_data = pd.DataFrame(post_dict)

    post_data.to_csv('file.csv')




   