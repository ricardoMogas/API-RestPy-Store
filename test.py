from DAO.ProductsDAO import ProductsDAO
from DAO.SessionDAO import SessionDAO
from core.dbConexion import dbConexion
from DAO.SalesDAO import SalesDAO
from DAO.SuppliersDAO import SuppliersDAO
from bson.objectid import ObjectId
from DAO.ConceptsDAO import ConceptsDAO


if __name__ == "__main__":
   #concepts = [
    #  {"productId": "66413933a075d4ca68e4991b", "quantity":1, "price":2500},
     # {"productId": "6641396ef6ac7fa256bd87c7", "quantity":4, "price":23},
     # {"productId": "664139e127e049f0516d318a", "quantity":2, "price":23}
   #]
   #sales = SalesDAO()
   #result = sales.RegisterSale("66373679da6cfb1ff4633082",2546,concepts)
   #result = sales.GetSaleOfCustomer("66373679da6cfb1ff4633082") 
    #usuarios = SessionDAO()
    #result = usuarios.GetUsersAll()
   #print(result)
    
   #producto = ProductsDAO()
   #result = producto.RegisterProduct("xbox", "1tb", "xbox.png", 7500, 7, "664139aa922a8c7cd9751ff7")
   #result = producto.ProductsBySupplier("664138f01eb552f3346a5d20")
   #print(result)
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

   #sale = SalesDAO()
   #result = sale.GetSaleOfCustomer("66373679da6cfb1ff4633082")
   #print(result)
   
   #supp = SuppliersDAO()
   #result = supp.RegisterSupplier("Microsoft", "Microsoft@gmail,com", 981004402, "L.A")
   #print(result)
   
   user = SessionDAO()
   result = user.login("m.angel_dzib@hotmail.com", 1234)
   print(result)
