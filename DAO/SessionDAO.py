from core.dbConexion import dbConexion
from bson.objectid import ObjectId
connection = dbConexion("localhost", 27017, "", "", "StoreDB_Distri")

class SessionDAO:
    def __init__(self, session = None):
        self.session = session

    def existName(self, username):
        connection.connect()
        query = {"name": username}
        result = connection.select("users", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                return True
            else:
                return False

    def existEmail(self, email):
        connection.connect()
        query = {"email": email}
        result = connection.select("users", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                return True
            else:
                return False


    def login(self, email, password):
        connection.connect()
        query = {"email": email, "password": password}
        result = connection.select("users", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                connection.disconnect()
                return result_list[0]["_id"] 
            else:
                connection.disconnect()
                return None 
        else:
            connection.disconnect()
        return None
        
    def register(self, username, email, password, rol):
        connection.connect()
        query = {"name": username, "email": email, "password": password,"rol": rol , "cart": []}
        result = connection.insert("users", query)
        connection.disconnect()
        return result.acknowledged
    
    def GetUsersAll(self):
        connection.connect()
        result = connection.select("users", {})
        users = []
        for item in result:
            usur = {
                "id": str(item["_id"]),
                "name": item["name"],
                "email": item["email"],
                "password": item["password"],
                "rol": item["rol"],
                "cart": item["cart"]
            }
            users.append(usur)
        return users
    
    def GetUserById(self, userId):
        connection.connect()
        query = {"_id": ObjectId(userId)}
        result = connection.select("users", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                connection.disconnect()
                return result_list[0]
            else:
                connection.disconnect()
                return None 
        else:
            connection.disconnect()
        return None



