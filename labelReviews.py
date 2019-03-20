#########################################################################
# Author: Neil Shah
# CMPE255 Assignment 1
# Description: Label each review as postive, negative or neutral based on 
#              positive/negative wordset from postive.txt and negative.txt
########################################################################


from sklearn.feature_extraction.text import CountVectorizer
import json


def labelReviews(filename):

    print("Labeling reviews as Positive/Negative/Neutral..")

    positiveWords=[]
    negativeWords=[]
    data = []
    corpus=[]
    wordsData=[]

    with open('./positiveWordset.txt') as f:
        for line in f: positiveWords.append(line.replace("\n",""))

    with open('./negativeWordset.txt') as f:
        for line in f: negativeWords.append(line.replace("\n",""))

    with open(filename) as f:
        for line in f: data.append(json.loads(line))

    for d in data: corpus.append(d["text"])

    for c in corpus:
        vectorizer = CountVectorizer(stop_words="english")
        X = vectorizer.fit_transform([c])
        wordsData.append(vectorizer.get_feature_names())


    for index,d in enumerate(wordsData):
        posAggregate=sum(el in d for el in positiveWords)
        negAggregate=sum(el in d for el in negativeWords)
        
        if(posAggregate - negAggregate < -1): data[index]["label"]="Negative"
        elif(posAggregate - negAggregate > 1): data[index]["label"] = "Positive"
        else: data[index]["label"] = "Neutral"

    with open(filename,'w') as f:
        for d in data:
            f.write(json.dumps(d))
            f.write("\n")
    f.close()


#labelReviews('./labeled_reviews.json')