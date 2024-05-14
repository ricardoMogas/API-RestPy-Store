import pymongo
import json
from config import MONGODB_URI, DATABASE_NAME, PORT_NUMBER

# Datos de conexión a la base de datos
client = pymongo.MongoClient("mongodb://"+MONGODB_URI+":"+str(PORT_NUMBER)+"/")
db = client[DATABASE_NAME]

# Función para leer un archivo JSON
def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Función para importar datos
def import_data(collection_name, filename):
    collection = db[collection_name]
    data = read_json(filename)
    collection.insert_many(data)
    print(f'Datos de {collection_name} insertados')

# Importar datos de users.json
import_data('users', 'core/dbJsons/users.json')

# Importar datos de products.json
import_data('products', 'core/dbJsons/products.json')

# Importar datos de sales.json
import_data('sales', 'core/dbJsons/sales.json')

# Importar datos de concepts.json
import_data('concepts', 'core/dbJsons/concepts.json')

# Importar datos de suppliers.json
import_data('suppliers', 'core/dbJsons/suppliers.json')

print("Proceso completado")
