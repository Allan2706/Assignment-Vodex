from database import item_collection, clock_in_collection
from schemas import Item, ClockInRecord
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo import ASCENDING
from typing import Optional


# Helper function to convert MongoDB document to Python dict
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "item_name": item["item_name"],
        "quantity": item["quantity"],
        "expiry_date": item["expiry_date"],
        "insert_date": item["insert_date"],
    }

# CRUD operations for Items
async def add_item(item_data: dict):
    item_data["insert_date"] = datetime.now()  
    result = await item_collection.insert_one(item_data)
    return item_helper(await item_collection.find_one({"_id": result.inserted_id}))


async def filter_items(email: Optional[str] = None, expiry_date: Optional[str] = None, 
                       insert_date: Optional[str] = None, quantity: Optional[int] = None):
    query = {}

    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}  
    if insert_date:
        query["insert_date"] = {"$gt": insert_date}  
    if quantity is not None:
        query["quantity"] = {"$gte": quantity}  
    items = []
    async for item in item_collection.find(query): 
        items.append(item_helper(item))
    
    return items


async def get_item(id: str):
    item = await item_collection.find_one({"_id": ObjectId(id)}) 
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")


async def delete_item(id: str):
    result = await item_collection.delete_one({"_id": ObjectId(id)}) 
    return result.deleted_count


async def update_item(id: str, item_data: dict):
    result = await item_collection.update_one({"_id": ObjectId(id)}, {"$set": item_data})  
    return result.modified_count


# CRUD Operations for Clock-In Records

def clock_in_helper(clock_in_data: dict) -> dict:
    return {
        "id": str(clock_in_data["_id"]),
        "email": clock_in_data["email"],
        "location": clock_in_data["location"],
        "insert_datetime": clock_in_data["insert_datetime"]
    }

async def add_clock_in(clock_in_data: dict):
    clock_in_data["insert_datetime"] = datetime.now()  
    result = await clock_in_collection.insert_one(clock_in_data)
    return clock_in_helper(await clock_in_collection.find_one({"_id": result.inserted_id}))


async def get_clock_in(id: str):
    clock_in = await clock_in_collection.find_one({"_id": ObjectId(id)})  
    if clock_in:
        return clock_in_helper(clock_in)
    raise HTTPException(status_code=404, detail="Clock-In Record not found")


async def filter_clock_ins(email: Optional[str] = None, location: Optional[str] = None, 
                            insert_datetime: Optional[str] = None):
    query = {}

    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": insert_datetime} 

    clock_ins = []
    async for clock_in in clock_in_collection.find(query): 
        clock_ins.append(clock_in_helper(clock_in))
    
    return clock_ins


async def delete_clock_in(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})  
    return result.deleted_count


async def update_clock_in(id: str, clock_in_data: dict):
    clock_in_data.pop("insert_datetime", None)  
    result = await clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": clock_in_data})
    return result.modified_count
