from fastapi import FastAPI, HTTPException
from schemas import Item, ClockInRecord
from crud import add_item, get_item, delete_item, add_clock_in
from crud import get_clock_in, delete_clock_in, update_item, update_clock_in

app = FastAPI()

# Items API
@app.post("/items/")
async def create_item(item: Item):
    new_item = await add_item(item.dict())
    return new_item

@app.get("/items/{id}")
async def read_item(id: str):
    item = await get_item(id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{id}")
async def remove_item(id: str):
    deleted_count = await delete_item(id)
    if deleted_count:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{id}")
async def update_existing_item(id: str, item: Item):
    updated_count = await update_item(id, item.dict())
    if updated_count:
        return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Clock-In Records API
@app.post("/clock-in/")
async def create_clock_in(clock_in: ClockInRecord):
    new_clock_in = await add_clock_in(clock_in.dict())
    return new_clock_in

@app.get("/clock-in/{id}")
async def read_clock_in(id: str):
    clock_in_record = await get_clock_in(id)
    if clock_in_record:
        return clock_in_record
    raise HTTPException(status_code=404, detail="Clock-In Record not found")

@app.delete("/clock-in/{id}")
async def remove_clock_in(id: str):
    deleted_count = await delete_clock_in(id)
    if deleted_count:
        return {"message": "Clock-In Record deleted successfully"}
    raise HTTPException(status_code=404, detail="Clock-In Record not found")

@app.put("/clock-in/{id}")
async def update_existing_clock_in(id: str, clock_in: ClockInRecord):
    updated_count = await update_clock_in(id, clock_in.dict())
    if updated_count:
        return {"message": "Clock-In Record updated successfully"}
    raise HTTPException(status_code=404, detail="Clock-In Record not found")
