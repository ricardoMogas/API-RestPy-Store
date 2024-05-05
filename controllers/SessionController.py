from core.dbConexion import dbConexion
connection = dbConexion("localhost", 27017, "", "", "StoreDB_Distri")

class SessionController:
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


    def login(self, username, password):
        connection.connect()
        query = {"name": username, "password": password}
        result = connection.select("users", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                connection.disconnect()
                return True
            else:
                connection.disconnect()
                return False
        
    def register(self, username, email, password):
        connection.connect()
        document = {"name": username, "email": email, "password": password, "cart": []}
        result = connection.insert("users", document)
        connection.disconnect()
        return result.acknowledged




