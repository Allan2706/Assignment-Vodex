import motor.motor_asyncio
# mongodb+srv://NIckNOah_157:<db_password>@cluster0.3jbs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
MONGO_DETAILS = "mongodb+srv://NIckNOah_157:NIckNOah_157@cluster0.3jbs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0.mongodb.net/Brightny"  # Replace with your MongoDB URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Brightny

item_collection = database.get_collection("items")
clock_in_collection = database.get_collection("clock_in_records")


# import motor.motor_asyncio

# # Replace <username>, <password>, and <mydatabase> with your actual MongoDB credentials and database name
# MONGO_DETAILS = "mongodb+srv://NIckNOah_157:<db_password>@cluster0.3jbs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
# database = client.mydatabase

# item_collection = database.get_collection("items")
# clock_in_collection = database.get_collection("clock_in_records")

