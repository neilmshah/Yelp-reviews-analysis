#########################################################################
# Author: Neil Shah
# CMPE255 Assignment 1
# Description: Main Program. 
#              Analyzes reviews and then predicts if a review is positive,
#              negative or neutral
########################################################################



import extractReviews
import labelReviews
import json


def load_data():
    data = []
    data_labels = []
    data_id = []

    with open("./labeled_reviews.json") as f:
        for i in f:
            review = json.loads(i)
            data.append(review['text'])
            data_labels.append(review['label'])
            data_id.append(review['business_id'])

    return data, data_labels, data_id


def transform_to_features(data):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(
        analyzer='word',
        lowercase=False,
    )
    features = vectorizer.fit_transform(
        data
    )
    features_nd = features.toarray()
    return features_nd


def train_then_build_model(data_labels, features_nd, data, data_id):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        features_nd,
        data_labels,
        train_size=0.80,
        random_state=1234)

    from sklearn.linear_model import LogisticRegression
    log_model = LogisticRegression()

    log_model = log_model.fit(X=X_train, y=y_train)
    y_pred = log_model.predict(X_test)

    restReview = {}

    featuresList = features_nd.tolist()

    for i in range(len(X_test)):
        index = featuresList.index(X_test[i].tolist())
        if(data_id[index] not in restReview.keys()):
            restReview[data_id[index]] = {'positive': 0, 'neutral': 0, 'negative': 0}

        if(y_pred[i] == 'Positive'): restReview[data_id[index]]['positive'] += 1
        elif(y_pred[i] == 'Negative'): restReview[data_id[index]]['negative'] += 1
        else: restReview[data_id[index]]['neutral'] += 1


    overallReview={}
    for id in restReview:
        restReview[id]=sorted(restReview[id].items(), key=lambda x:x[1], reverse=True)
        overallReview[id]=restReview[id][0][0]

    yelpReview = {}
    with open('./restaurants.json') as rest:
        for i in rest:
            yelp_r = json.loads(i)
            yelpReview[yelp_r['business_id']] = yelp_r['stars']

    for id in restReview:
        print("{}: Predition: {} ; Yelp's Rating: {}".format(id, overallReview[id], yelpReview[id]))


    from sklearn.metrics import accuracy_score, confusion_matrix
    import numpy as np

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    recall = np.diag(cm) / np.sum(cm, axis=1)
    precision = np.diag(cm) / np.sum(cm, axis=0)
    recall = np.mean(recall)
    precision = np.mean(precision)
    f1score = (2*precision*recall)/(precision+recall)
    print("Accuracy= {}".format(accuracy))
    print("Precision= {}".format(precision))
    print("Recall= {}".format(recall))
    print("F1-score= {}".format(f1score))

    from sklearn.model_selection import cross_val_score
    print("Cross Validation Score= {}\n".format(cross_val_score(
        log_model, X_train, y_train, cv=3, scoring="accuracy")))

    # from sklearn.metrics import accuracy_score
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy={}".format(accuracy))


def process():
    extractReviews.extract_json()
    labelReviews.labelReviews('./labeled_reviews.json')

    data, data_labels, data_id = load_data()
    features_nd = transform_to_features(data)
    train_then_build_model(data_labels, features_nd, data, data_id)



process()
