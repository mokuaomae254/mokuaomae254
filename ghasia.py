import streamlit as st
import tweepy
import csv
from textblob import TextBlob


class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def clean_tweet(self, tweet):
        # Utility function to clean tweet text by removing links, special characters using simple regex statements.
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def download_data(self, search_term, num_of_terms):
        # Authenticating
        consumer_key = st.secrets['twitter']['consumer_key']
        consumer_secret = st.secrets['twitter']['consumer_secret']
        access_token = st.secrets['twitter']['access_token']
        access_token_secret = st.secrets['twitter']['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Searching for tweets
        self.tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang="en").items(num_of_terms)

        # Open/create a file to append data to
        csv_file = open('result.csv', 'a')

        # Use csv writer
        csv_writer = csv.writer(csv_file)

        # Creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0

        # Iterating through tweets fetched
        for tweet in self.tweets:
            # Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.clean_tweet(tweet.text).encode('utf-8'))
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity  # Adding up polarities to find the average later

            # Adding reaction of how people are reacting to find average later
            if analysis.sentiment.polarity == 0:
                neutral += 1
            elif 0 < analysis.sentiment.polarity <= 0.3:
                wpositive += 1
            elif 0.3 < analysis.sentiment.polarity <= 0.6:
                positive += 1
            elif 0.6 < analysis.sentiment.polarity <= 1:
                spositive += 1
            elif -0.3 < analysis.sentiment.polarity <= 0:
                wnegative += 1
            elif -0.6 < analysis.sentiment.polarity <= -0.3:
                negative += 1
            elif -1 < analysis.sentiment.polarity <= -0.6:
                snegative += 1

        # Write to csv and close csv file
        csv_writer.writerow(self.tweetText)
        csv_file.close()

        # Finding average of how people are reacting
        positive = self.percentage(positive, num_of_terms)
        wpositive = self.percentage(wpositive, num_of_terms)
        spositive = self.percentage(spositive, num_of_terms)
        negative = self.percentage(negative, num_of_terms)
        wnegative = self.percentage(wnegative, num_of_terms)
        snegative = self.percentage(snegative, num_of_terms)
        neutral = self.percentage(neutral, num_of_terms)

        # Finding average reaction
        

        polarity = polarity / NoOfTerms

        # printing out data
        st.write("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        st.write("")
        st.write("General Report: ")

        if (polarity == 0):
            st.write("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            st.write("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            st.write("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            st.write("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            st.write("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            st.write("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            st.write("Strongly Negative")

        st.write("")
        st.write("Detailed Report: ")
        st.write(str(positive) + "% people thought it was positive")
        st.write(str(wpositive) + "% people thought it was weakly positive")
        st.write(str(spositive) + "% people thought it was strongly positive")
        st.write(str(negative) + "% people thought it was negative")
        st.write(str(wnegative) + "% people thought it was weakly negative")
        st.write(str(snegative) + "% people thought it was strongly negative")
        st.write(str(neutral) + "% people thought it was neutral")

        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)
    def clean_tweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())    
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
        fig, ax = plt.subplots()
        ax.pie(sizes, colors=colors, startangle=90)
        ax.legend(labels, loc="best")
        ax.set_title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
        ax.axis('equal')
        st.pyplot(fig)
if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
#streamlit run ghasia.py