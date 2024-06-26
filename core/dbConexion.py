from pymongo import MongoClient
from bson.objectid import ObjectId

class dbConexion:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
            self.db = self.client[self.database]
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def disconnect(self):
        try:
            self.client.close()
            print("Disconnected from MongoDB")
        except Exception as e:
            print(f"Error disconnecting from MongoDB: {e}")

    def select(self, collection, query):
        try:
            return self.db[collection].find(query)
        except Exception as e:
            print(f"Error executing select query: {e}")

    def insert(self, collection, document):
        try:
            return self.db[collection].insert_one(document)
        except Exception as e:
            print(f"Error executing insert query: {e}")

    def update(self, collection, query, update):
        try:
            return self.db[collection].update_many(query, update)
        except Exception as e:
            print(f"Error executing update query: {e}")

    def delete(self, collection, query):
        try:
            return self.db[collection].delete_many(query)
        except Exception as e:
            print(f"Error executing delete query: {e}")

# Ejemplo de uso
"""
if __name__ == "__main__":
    connection = dbConexion("localhost", 27017, "", "", "StoreDB_Distri")
    connection.connect()

    # Select example
    query = {"name": "Juan"}
    result = connection.select("users", query)
    for document in result:
        print(document.get("name"))


    # insert example
    document = {"name": "test4", "email": "test4@example.com", "password": "1234", "cart": []}
    result = connection.insert("users", document)
    print(result.acknowledged)


    # update example
    # query = {"_id": ObjectId("6635a9f9d069d60327f1ca50")}
    # update = {"$set": {"password": "321"}}
    # result = connection.update("users", query, update)
    # print(result)

    
    connection.disconnect()
"""