from pymongo import MongoClient

class MongoDBConnection:
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
if __name__ == "__main__":
    connection = MongoDBConnection("localhost", 27017, "username", "password", "mydatabase")
    connection.connect()

    # Select example
    query = {"name": "John"}
    result = connection.select("users", query)
    for document in result:
        print(document)

    # Insert example
    document = {"name": "Jane", "age": 25}
    connection.insert("users", document)

    # Update example
    query = {"name": "John"}
    update = {"$set": {"age": 30}}
    connection.update("users", query, update)

    # Delete example
    query = {"name": "Jane"}
    connection.delete("users", query)

    connection.disconnect()