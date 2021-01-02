import pymongo
import os, sys
from bson.objectid import ObjectId

connectionUri = os.environ.get('chatreMongoConnectionUri')
cluster = pymongo.MongoClient(connectionUri)
db = cluster["users"]
follow_collection = db["follow"]

def follow(follower, following):
    follow_collection.insert_one({
        "follower":ObjectId(follower),
        "following":ObjectId(following)
    })

def unfollow(follower, following):
    follow_collection.delete_one({
        "follower":ObjectId(follower),
        "following":ObjectId(following)
    })

def is_following(follower, following):
    follow = follow_collection.find({
        "follower":ObjectId(follower),
        "following":ObjectId(following)
    }).count()

    return follow

def count_followers(following):
    query = {"following":following}
    query_results = follow_collection.count_documents(query)
    return query_results