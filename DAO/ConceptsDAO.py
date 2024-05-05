from core.dbConexion import dbConexion
connection = dbConexion("localhost", 27017, "", "", "StoreDB_Distri")

class ConceptsDAO:
    def __init__(self, session = None):
        self.session = session
    
    def GetConceptsAll(self):
        connection.connect()
        result = connection.select("concepts", {})
        concepts = []
        for item in result:
            concept = {
                "id": str(item["_id"]),
                "saleId": str(item["saleId"]),
                "productId": item["productId"],
                "import": item["import"],
                "quantity": item["cuantity"],
                "price": item["price"]
            }
            concepts.append(concept)
        return concepts
