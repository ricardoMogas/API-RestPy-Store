from core.dbConexion import dbConexion
import json
from datetime import datetime
from bson.objectid import ObjectId
from DAO.ProductsDAO import ProductsDAO
from DAO.ConceptsDAO import ConceptsDAO
from DAO.SessionDAO import SessionDAO
from typing import List
from config import MONGODB_URI, DATABASE_NAME, PORT_NUMBER
connection = dbConexion(MONGODB_URI, DATABASE_NAME)

class SalesDAO:
    def __init__(self):
        pass

    def RegisterSale(self, userId, total, concepts: List[dict] ):
        connection.connect()
        query = {"Datetime": datetime.now(), "userId": userId, "total":total}
        result = connection.insert("sales", query)
        saleId = result.inserted_id 
        for requestConcept in concepts:
            product = ProductsDAO()
            producto = product.GetProductsById(requestConcept["productId"])
            conceptNew = {
                "quantity": requestConcept["quantity"],
                "saleId": saleId,
                "productId": requestConcept["productId"],
                "price": requestConcept["price"],
                "import": requestConcept["quantity"] * requestConcept["price"]
            }
            result = connection.insert("concepts", conceptNew)
            stockNow = producto["stock"] - requestConcept["quantity"]
            stockUpdate = product.UpdateProduct(requestConcept["productId"], stock=stockNow)
            
        return result.acknowledged
    
    def GetSaleOfCustomer(self, userId):
        connection.connect()
        query = {"userId": userId}
        result = connection.select("sales", query)
        sales = list(result)
        listSales = []

        for sale in sales:
            query2 = {"saleId": sale["_id"]}
            result2 = connection.select("concepts", query2)
            concepts = list(result2)
            saleInfo = {
                "_id": str(sale["_id"]),
                "Datetime": sale["Datetime"],
                "total": sale["total"],
                "concepts": []
            }

            for concept in concepts:
                products = ProductsDAO()
                product = products.GetProductsById(concept["productId"])
                conceptInfo = {
                    "product": product["name"],
                    "image": product["image"],
                    "description": product["description"],
                    "quantity": concept["quantity"],
                    "import": concept["import"]
                }
                saleInfo["concepts"].append(conceptInfo)
            listSales.append(saleInfo)
        return listSales

        