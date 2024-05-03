from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.0},
    {"id": 2, "nombre": "Producto 2", "precio": 20.0}
]

@app.route('/')
def index():
    return "API de productos"

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    usuario = request.json
    if usuario['user'] == 'root' and usuario['password'] == '123':
        return jsonify({'mensaje': 'Inicio de sesión correcto'})
    else:
        return jsonify({'mensaje': 'Inicio de sesión incorrecto'}), 401


# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

# Ruta para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.json
    productos.append(nuevo_producto)
    return jsonify({'mensaje': 'Producto agregado correctamente'}), 201

# Ruta para actualizar un producto existente
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    producto_actualizado = request.json
    for i, p in enumerate(productos):
        if p['id'] == producto_id:
            productos[i] = producto_actualizado
            return jsonify({'mensaje': 'Producto actualizado correctamente'})
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

# Ruta para eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    for i, p in enumerate(productos):
        if p['id'] == producto_id:
            del productos[i]
            return jsonify({'mensaje': 'Producto eliminado correctamente'})
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
