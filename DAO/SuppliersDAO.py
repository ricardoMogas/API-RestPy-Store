from core.dbConexion import dbConexion
from bson.objectid import ObjectId
import json
from config import MONGODB_URI, DATABASE_NAME, PORT_NUMBER
connection = dbConexion(MONGODB_URI, PORT_NUMBER, "", "", DATABASE_NAME)

class SuppliersDAO:
    def __init__(self):
        pass

    def GetSuppliers(self):
        connection.connect()
        result = connection.select("suppliers", {})
        suppliers = []
        for item in result:
            supplier = {
                "id": str(item["_id"]),
                "name": item["name"],
                "email": item["email"],
                "number": item["number"],
                "address": item["address"]
            }
            suppliers.append(supplier)
        return suppliers
    
    def GetSupplierById(self, supplierId):
        connection.connect()
        query = {"_id": ObjectId(supplierId)}
        result = connection.select("suppliers", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                return result_list[0]  
            else:
                return None 
        else:
            return None
    
    def RegisterSupplier(self,name, email, number, address):
        connection.connect()
        query = {
                "name": name,
                "email": email,
                "number": number,
                "address": address
            }
        result = connection.insert("suppliers", query)
        connection.disconnect()
        return result.acknowledged
    
    def DeleteSupplier(self, supplierId):
        connection.connect()
        query = {"_id": ObjectId(supplierId)}
        result = connection.delete("suppliers", query)
        connection.disconnect()
        return result.deleted_count > 0

    def UpdateSupplier(self, supplierId, name=None, email=None, number=None, address=None):
        connection.connect()
        query = {"_id": ObjectId(supplierId)}
        updateQuery = {"$set": {}}

        if name is not None:
            updateQuery["$set"]["name"] = name
        if email is not None:
            updateQuery["$set"]["email"] = email
        if number is not None:
            updateQuery["$set"]["number"] = number
        if address is not None:
            updateQuery["$set"]["address"] = address
        
        result = connection.update("suppliers", query, updateQuery)
        connection.disconnect()
        return result.acknowledged

