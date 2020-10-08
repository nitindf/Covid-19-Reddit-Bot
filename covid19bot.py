import requests
import json
import praw

def get_data():
    result=requests.get("https://api.covid19india.org/state_district_wise.json")
    data=json.loads(result.text)
    data=result.json()
    chennai_total=data['Tamil Nadu']['districtData']['Chennai']
    data = f''' Active cases : {chennai_total["active"]}
    
|  |Total|
|:--:|:--:|
|Confirmed|{chennai_total['confirmed']}|
|Recovered|{chennai_total['recovered']}|
|Deceased|{chennai_total['deceased']}|'''
    
    return data

def main():
    reddit = praw.Reddit(client_id=" ",    # Generated after creating Reddit App
                         client_secret=" ",# Generated after creating Reddit App
                         user_agent=" ",   # Enter unique string.(Eg "console:covid-19:1.0")
                         username=" ",     # Enter reddit account's username
                         password=" ")     # Enter rediit account's password
    
    subreddit=reddit.subreddit("Chennai")
    
    for comment in subreddit.stream.comments(skip_existing=True):
        
        if hasattr(comment,"body"):
            comment_lower=comment.body.lower()
            
            if "!cases" in comment_lower:
                data=get_data()
                comment.reply(data)
                
    return 0

if __name__ == "__main__":
    main()
