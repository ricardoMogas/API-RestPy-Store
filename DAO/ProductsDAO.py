from core.dbConexion import dbConexion
import json
connection = dbConexion("localhost", 27017, "", "", "StoreDB_Distri")

class ProductsDAO:
    def __init__(self):
        pass

    def GetProducts(self):
        connection.connect()
        result = connection.select("products", {})
        products = []
        for item in result:
            product = {
                "id": str(item["_id"]),
                "name": item["name"],
                "description": item["description"],
                "image": item["image"],
                "cost": item["cost"],
                "stock": item["stock"]
            }
            products.append(product)
        return products
