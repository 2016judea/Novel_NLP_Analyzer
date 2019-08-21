"""
ALJ 08/21/2019 -> Short program for running NLP analysis per paragraph of a textfile (novel in this case taken from ProjectGutenberg)
                  We plot the results afterward for high level analysis


Library Documentation: 
    TextBlob = https://textblob.readthedocs.io/en/dev/

"""

from textblob import TextBlob
import matplotlib.pyplot as plt

def main():
    #novel we want to run NLP analysis on
    novel = "ThisSideOfParadise.txt"
    #read in the novel specified as a string
    f = open(novel, 'r')
    novel_as_string = f.read()
    f.close()

    paragraphs = novel_as_string.split("\n\n")
    sentiment_value = []
    sentiment_position = []
    x = 0

    for single_para in paragraphs:
        x += 1
        #utilize TextBlob for NLP
        blob = TextBlob(single_para)
        sentiment_value.append(blob.sentiment.polarity)
        sentiment_position.append(x)
        #delete TextBlob object for sake of OS efficiency
        del blob

    plt.plot(sentiment_position, sentiment_value)
    plt.xlabel('Novel by Paragraph')
    plt.ylabel('Sentiment')
    plt.show()
    

if __name__ == "__main__":
    main()

