from random import randint
import tweepy
import spacy
nlp = spacy.load("en_core_web_sm")

api_key = "XtnzGkdzHQ5oj4H8GUbVb1q7R"
api_secret = "Il3WEFCpmjTu21KVWCcI47eGYr9qhGbsIP18bFaTjo9MISfjmd"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACZ8kQEAAAAAellyfD%2FN5F5NdqzjekGW0SjK1WA%3DRMERilpZmqcn6ez0jjRmtGX87i0QDVyiAJwleMr1gqBw5b7sLS"
access_token = "1602380513716600841-o5tPh1OVHANh7lurze4SoNpEOIvnqF"
access_token_secret = "1ZkqGaqJrK07xGGzMG95Xp2yZ38npLjj2cCDwq8KxOefG"


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


f = open('/Users/nickmountain/Twitter-bot-workspace/Things/taylor.txt', 'r')
lines: list[str] = f.readlines()
f.close()


def write_tweet(lines: list[str]) -> str:
    send_tweet: bool = False
    number = randint(0, len(lines)-1)
    line = lines[number]
    line_list = line.split(' ')
    for word in range(len(line_list)):
        
        text = line_list[word]
        doc = nlp(text)
        if (doc[0].tag_ == 'NNP'):
            send_tweet = True
            #print('found a noun')
            #print(f"The line was: {line}")
            print(f"The noun was: {line_list[word]}")
            line_list[word] = 'Nunez'
        #print(word)
    
    message = ' '.join(line_list)
    if not send_tweet:
        message = write_tweet(lines)

    return message


tweet = write_tweet(lines)
print(tweet)

def write_tweet():
    api.update_status(tweet)


if __name__ == '__main__':
    write_tweet()