from DAO.ProductsDAO import ProductsDAO
from DAO.SessionDAO import SessionDAO
from core.dbConexion import dbConexion
from DAO.SalesDAO import SalesDAO
from bson.objectid import ObjectId
from DAO.ConceptsDAO import ConceptsDAO


if __name__ == "__main__":
    '''
    concepts = [
        {"productId": "6637cd15e24066094544c72e", "quantity":1, "price":2500},
        {"productId": "663718fe88cffad56cc07cb8", "quantity":4, "price":23},
        {"productId": "663718fe88cffad56cc07cb7", "quantity":2, "price":23}
    ]
    sales = SalesDAO()
    result = sales.RegisterSale("66373679da6cfb1ff4633082",500,concepts)
    '''

    #usuarios = SessionDAO()
    #result = usuarios.GetUsersAll()
    #print(result)
    
    producto = ProductsDAO()
    result = producto.RegisterProduct("Targeta Grafica GT 710", "Targeta de video con 2gb de vram ddr3 muy util para pc de oficina y de uso ligero", "xbox.png", 1999, 5)
    print(result)
    #result = producto.UpdateProduct("6637cd15e24066094544c72e", name= "playstation")
    #result = producto.GetProductsById("6637cd15e24066094544c72e")
    #print(result["name"])

