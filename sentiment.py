from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import codecs

with codecs.open('Sample.txt', encoding='utf-8') as f:
    sentences = f.readlines()
for sentence in sentences:
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(sentence)
    
    print("\nDictionary=",sentiment_dict)
    if sentiment_dict['compound'] >= 0.05 :
            print("It is a Positive Sentence")
             
    elif sentiment_dict['compound'] <= - 0.05 :
            print("It is a Negative Sentence")      
    else :    
           print("It is a Neutral Sentence")
