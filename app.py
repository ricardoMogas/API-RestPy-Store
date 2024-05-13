from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from DAO.SessionDAO import SessionDAO
from DAO.ProductsDAO import ProductsDAO
from DAO.SuppliersDAO import SuppliersDAO
from DAO.SalesDAO import SalesDAO
from bson.json_util import dumps
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "API de productos"


# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]
    session = SessionDAO()
    if session.login(email, password):
        return jsonify({"status": True, "message": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"status": False, "message": "Inicio de sesión fallido: contraseña o correo incorrecto"}), 400


# Ruta para obtener todos los productos
@app.route('/register', methods=['POST'])
def user_register():
    data = request.get_json()
    name = data["username"]
    email = data["email"]
    password = data["password"]
    rol = 1
    session = SessionDAO()
    if session.existName(name) and session.existEmail(email):
        return jsonify({"status": False, "message": "Ya existe ese usuario o email"}), 400

    result = session.register(name, email, password, rol)
    return jsonify({"status": result, "message:": "Registro completo"}), 201


@app.route('/GetAllProducts', methods=['GET'])
def GetProducts():
    products = ProductsDAO()
    result = products.GetProducts()
    if result is None:
        return jsonify({"status": False, "message": "No hay productos"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200

@app.route('/RegisterProduct', methods=['POST'])
def RegisterProducts():
    data = request.get_json()
    products = ProductsDAO()
    result = products.RegisterProduct(data["name"], data["description"], data["image"], data["price"], data["stock"], data["supplierId"])
    if result is None:
        return jsonify({"status": False, "message": "Error"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/DeleteProduct/<product_id>', methods=['DELETE'])
def DeleteProducts(product_id):
    products = ProductsDAO()
    result = products.DeleteProduct(product_id)
    if result is None:
        return jsonify({"status": False, "message": "No hay producto"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/UpdateProduct/', methods=['PUT'])
def UpdateProducts():
    data = request.get_json()
    products = ProductsDAO()
    result = products.UpdateProduct(data["id"], data["name"], data["description"], data["image"], data["price"], data["stock"], data["supplierId"])
    if result is None:
        return jsonify({"status": False, "message": "No se actualizo producto"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/GetAllSuppliers', methods=['GET'])
def GetSuppliers():
    suppliers = SuppliersDAO()
    result = suppliers.GetProducts()
    if result is None:
        return jsonify({"status": False, "message": "No hay proveedores"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200

@app.route('/RegisterSuppliers', methods=['POST'])
def RegisterProducts():
    data = request.get_json()
    supplier = SuppliersDAO()
    result = supplier.RegisterSupplier(data["name"], data["gmail"], data["number"], data["address"])
    if result is None:
        return jsonify({"status": False, "message": "Error"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/DeleteSupplier/<supplierId>', methods=['DELETE'])
def DeleteProducts(supplierId):
    supplier = SuppliersDAO()
    result = supplier.DeleteSupplier(supplierId)
    if result is None:
        return jsonify({"status": False, "message": "No hay proveedor"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/UpdateSupplier', methods=['PUT'])
def UpdateProducts():
    data = request.get_json()
    supplier = SuppliersDAO()
    result = supplier.UpdateSupplier(data["id"], data["name"], data["email"], data["number"], data["address"])
    if result is None:
        return jsonify({"status": False, "message": "No se actualizo proveedor"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200

@app.route('/GetSalesCustomer', methods=['GET'])
def GetSales():
    data = request.get_json()
    sales = SalesDAO()
    result = sales.GetSaleOfCustomer(data["userId"])
    if result is None:
        return jsonify({"status": False, "message": "No hay compras"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
    
@app.route('/RegisterSales', methods=['POST'])
def RegisterSaless():
    data = request.get_json()
    sales = SalesDAO()
    result = sales.RegisterSale(data["userId"], data["total"], data["concepts"])
    if result is None:
        return jsonify({"status": False, "message": "Error"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200
if __name__ == '__main__':
    app.run(debug=True)
