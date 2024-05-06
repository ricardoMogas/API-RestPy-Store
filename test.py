from DAO.ProductsDAO import ProductsDAO
from DAO.SessionDAO import SessionDAO
from core.dbConexion import dbConexion
from DAO.SalesDAO import SalesDAO
from bson.objectid import ObjectId
from DAO.ConceptsDAO import ConceptsDAO


if __name__ == "__main__":
   #concepts = [
   #   {"productId": "6637cd15e24066094544c72e", "quantity":1, "price":2500},
   #   {"productId": "663718fe88cffad56cc07cb8", "quantity":4, "price":23},
   #   {"productId": "663718fe88cffad56cc07cb7", "quantity":2, "price":23}
   #]
   #sales = SalesDAO()
   #result = sales.RegisterSale("6637192b88cffad56cc07cba",500,concepts)
    
    #usuarios = SessionDAO()
    #result = usuarios.GetUsersAll()
    #print(result)
    
    #producto = ProductsDAO()
    #result = producto.RegisterProduct("Xbox", "Xbox one con 1tb", "xbox.png", 3000, 4)
    #result = producto.UpdateProduct("6637cd15e24066094544c72e", name= "playstation")
    #result = producto.GetProductsById("6637cd15e24066094544c72e")
    #print(result["name"])
    #user = SessionDAO()
    #result = user.GetUserById("66373679da6cfb1ff4633082")
    #print(result)
    
   #concepto = ConceptsDAO()
   #result = concepto.GetConceptsAll()
   #print(result)
    #producto = ProductsDAO()
    #result = producto.GetProducts()
    #print(result)

   sale = SalesDAO()
   result = sale.GetSaleOfCustomer("66373679da6cfb1ff4633082")
   print(result)
