from pymongo import MongoClient

uri = "mongodb+srv://<saurabhkk5585_db_user>:<45bRL8Uk4HxxY3m2>@cluster0.20rolkm.mongodb.net/"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("Connection failed:", e)