from DAO.SessionDAO import SessionController
from DAO.ProductsDAO import ProductsDAO
from core.dbConexion import dbConexion
from bson.objectid import ObjectId

if __name__ == "__main__":
    
    products = ProductsDAO()
    result = products.GetProducts()
    print(result[0]["name"])


