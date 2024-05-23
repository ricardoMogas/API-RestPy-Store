from pymongo import MongoClient
from bson.objectid import ObjectId

class dbConexion:
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.database]
            print(f"Connected to MongoDB, using database: {self.database}")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def disconnect(self):
        try:
            if self.client:
                self.client.close()
                print("Disconnected from MongoDB")
        except Exception as e:
            print(f"Error disconnecting from MongoDB: {e}")

    def select(self, collection, query):
        try:
            if self.db is not None:
                return self.db[collection].find(query)
            else:
                print("Error: Not connected to any database.")
                return None
        except Exception as e:
            print(f"Error executing select query: {e}")
            return None

    def insert(self, collection, document):
        try:
            if self.db is not None:
                return self.db[collection].insert_one(document)
            else:
                print("Error: Not connected to any database.")
                return None
        except Exception as e:
            print(f"Error executing insert query: {e}")
            return None

    def update(self, collection, query, update):
        try:
            if self.db is not None:
                return self.db[collection].update_many(query, update)
            else:
                print("Error: Not connected to any database.")
                return None
        except Exception as e:
            print(f"Error executing update query: {e}")
            return None

    def delete(self, collection, query):
        try:
            if self.db is not None:
                return self.db[collection].delete_many(query)
            else:
                print("Error: Not connected to any database.")
                return None
        except Exception as e:
            print(f"Error executing delete query: {e}")
            return None


# Ejemplo de uso
'''
if __name__ == "__main__":
    uri = "mongodb+srv://ricardoMogas:nmMfdujq7ZiFVWtG@cluster0.buubtnc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    db = "StoreDB_Distri"
    connection = dbConexion(uri, db)
    connection.connect()

    # Select example
    query = {}
    result = connection.select("users", query)
    if result is not None:
        for document in result:
            print(document)
'''

    # Insert example
    # document = {"name": "test4", "email": "test4@example.com", "password": "1234", "cart": []}
    # result = connection.insert("users", document)
    # if result is not None:
    #     print(result.acknowledged)

    # Update example
    # query = {"_id": ObjectId("6635a9f9d069d60327f1ca50")}
    # update = {"$set": {"password": "321"}}
    # result = connection.update("users", query, update)
    # if result is not None:
    #     print(result.modified_count)

    ## connection.disconnect()
