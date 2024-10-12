import motor.motor_asyncio
MONGO_DETAILS = "mongodb+srv://NIckNOah_157:NIckNOah_157@cluster0.3jbs7.mongodb.net/Brightny?retryWrites=true&w=majority&appName=Cluster0&ssl=false"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Brightny

item_collection = database.get_collection("items")
clock_in_collection = database.get_collection("clock_in_records")





