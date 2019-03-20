#########################################################################
# Author: Neil Shah
# CMPE255 Assignment1
# Description: Use pre-defined positive and negative words 
#              to classify reviews into positive, negative and neutral
########################################################################

import json
import operator

#extract restuarant business IDs from business.json 
def filter_restaurants():
    print("Filtering Restaurants..")
    restaurants = open('restaurants.json', 'w')
    with open('./business.json') as f:
        for business in f:
            business_data = json.loads(business)
            business_id = business_data['business_id']
            categories = business_data['categories']
            if categories and 'Restaurants' in categories:
                restaurants.write(json.dumps(
                    {'business_id': business_id, 'stars': business_data['stars']}))
                restaurants.write('\n')
    f.close()
    restaurants.close()

#Sort the reviews by business ID 
def sortData(filename):
    print("Sorting Reviews by Restaurant ID..")
    reviews = []
    with open(filename) as f:
        for i in f: reviews.append(json.loads(i))
    f.close()
    reviews.sort(key=operator.itemgetter('business_id'))
    with open(filename, 'w') as f:
        for r in reviews:
            f.write(json.dumps(r))
            f.write('\n')
    f.close()

# Create new dataset of 15000 reviews
# as program crashes if there are too many
def extract_json():
    filter_restaurants()

    print("Extracting reviews based on Restaurant ID..")

    traning_set = open('labeled_reviews.json', 'w')
    restaurants = []
    
    with open('./restaurants.json') as rest:
        for i in rest:
            rest_data = json.loads(i)
            restaurants.append(rest_data['business_id'])
    
    with open('./review.json') as f:
        reviewCount=0
        for review in f:
            if(reviewCount==15000): break
            data = json.loads(review)
            if data['business_id'] not in restaurants: continue

            currReview = {
                'business_id': data['business_id'], 'text': (data['text']).replace('\n', ' ').replace('\r', '').strip()}
            traning_set.write(json.dumps(currReview))
            traning_set.write('\n')
            reviewCount += 1

    traning_set.close()
    sortData('./labeled_reviews.json')


#extract_json()
