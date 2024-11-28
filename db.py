from pymongo import MongoClient
from config import *
import json

client=MongoClient(DB_URI)
db=client[DB_NAME]
col=db[DB_NAME]

cf = col.find_one({'_id':DB_NAME})

if not cf: cf={'_id':DB_NAME}

async def sync():
        col.replace_one({'_id':DB_NAME} , cf , upsert=True)