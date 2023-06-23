from textblob import TextBlob

# blob = TextBlob("I Hate you")

# print(blob.sentiment.polarity)

def get_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    if score >= 0.5:
        return 'This sentence is Positive'
    elif score >= 0.05 and score < 0.5:
        return 'This sentence is Partially Positive'
    elif score > -0.05 and score < 0.05:
        return 'This sentence is Neutral'
    elif score > -0.5 and score <= -0.05:
        return 'This sentence is Partially Negative'
    else:
        return 'This sentence is Negative'
    
print(get_sentiment("I love you but you hate me"))