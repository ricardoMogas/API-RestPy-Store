from core.dbConexion import dbConexion
from bson.objectid import ObjectId
import json
from DAO.SuppliersDAO import SuppliersDAO
from config import MONGODB_URI, DATABASE_NAME, PORT_NUMBER
connection = dbConexion(MONGODB_URI, DATABASE_NAME)

class ProductsDAO:
    def __init__(self):
        pass

    def GetProducts(self):
        connection.connect()
        result = connection.select("products", {})
        products = []
        for item in result:
            result = SuppliersDAO().GetSupplierById(item["supplierId"])
            product = {
                "id": str(item["_id"]),
                "name": item["name"],
                "description": item["description"],
                "image": item["image"],
                "price": item["price"],
                "stock": item["stock"],
                "nameSupplier": (result["name"] if result is not None else ""),
                "supplierId": item["supplierId"]
            }
            products.append(product)
        connection.disconnect()
        return products
    
    def GetProductsById(self, productId):
        connection.connect()
        query = {"_id": ObjectId(productId)}
        result = connection.select("products", query)
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
    
    def RegisterProduct(self,name, description, image, price, stock, supplierId):
        connection.connect()
        query = {
                "name": name,
                "description": description,
                "image": image,
                "price": price,
                "stock": stock,
                "supplierId": supplierId
            }
        result = connection.insert("products", query)
        connection.disconnect()
        return result.acknowledged
    
    def DeleteProduct(self, product_id):
        connection.connect()
        query = {"_id": ObjectId(product_id)}
        result = connection.delete("products", query)
        connection.disconnect()
        return result.deleted_count > 0

    def UpdateProduct(self, productId, name=None, description=None, image=None, price=None, stock=None, supplierId=None):
        connection.connect()
        query = {"_id": ObjectId(productId)}
        updateQuery = {"$set": {}}

        if name is not None:
            updateQuery["$set"]["name"] = name
        if description is not None:
            updateQuery["$set"]["description"] = description
        if image is not None:
            updateQuery["$set"]["image"] = image
        if price is not None:
            updateQuery["$set"]["price"] = price
        if stock is not None:
            updateQuery["$set"]["stock"] = stock
        if supplierId is not None:
            updateQuery["$set"]["supplierId"] = supplierId
        
        result = connection.update("products", query, updateQuery)
        connection.disconnect()
        return result.acknowledged
    
    def ProductsBySupplier(self, supplierId):
        connection.connect()
        query = {"supplierId": supplierId}
        result = connection.select("products", query)
        if result is not None:
            result_list = list(result)
            if len(result_list) > 0:
                connection.disconnect()
                return result_list  
            else:
                connection.disconnect()
                return None 
        else:
            connection.disconnect()
        return None

