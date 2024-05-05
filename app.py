from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from DAO.SessionDAO import SessionDAO
from DAO.ProductsDAO import ProductsDAO
from bson.json_util import dumps
app = Flask(__name__)


@app.route('/')
def index():
    return "API de productos"


# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    session = SessionController()
    if session.login(username, password):
        return jsonify({"status": True, "message": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"status": False, "message": "Inicio de sesión fallido: contraseña o usuario incorrecto"}), 400
    

# Ruta para obtener todos los productos
@app.route('/register', methods=['POST'])
def user_register():
    data = request.get_json()
    name = data["username"]
    email = data["email"]
    password = data["password"]
    session = SessionController()
    if session.existName(name) and session.existEmail(email):
        return jsonify({"status": False, "message": "Ya existe ese usuario o email"}), 400

    result = session.register(name, email, password)
    return jsonify({"status": result, "message:": "Registro completo"}), 201


@app.route('/GetAllProducts', methods=['GET'])
def GetProducts():
    products = ProductsDAO()
    result = products.GetProducts()
    if result is None:
        return jsonify({"status": False, "message": "No hay productos"}), 404
    else:
        return jsonify({"status":True, "data": result}), 200

@app.route('/saleProduct', methods=['GET'])
def saleProduct():
    return jsonify({"status": True, "message": "Producto vendido"}), 200

@app.route('/addProduct', methods=['POST'])
def addProduct():
    return jsonify({"status": True, "message": "Producto agregado"}), 200

if __name__ == '__main__':
    app.run(debug=True)
