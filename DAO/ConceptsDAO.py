from core.dbConexion import dbConexion
from config import MONGODB_URI, DATABASE_NAME, PORT_NUMBER
connection = dbConexion(MONGODB_URI, PORT_NUMBER, "", "", DATABASE_NAME)

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
                "quantity": item["quantity"],
                "price": item["price"]
            }
            concepts.append(concept)
        return concepts
