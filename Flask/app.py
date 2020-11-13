from flask import Flask, jsonify

app = Flask(__name__)

from products import products

# Definición de rutas
@app.route('/ping')
def ping():
    return jsonify({'message':'Pong'})

#
@app.route('/products')
def getProducts():
    return jsonify({"products":products, "message":"Product's list"})
    
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    product_found = [product for product in products if product['name']==product_name]
    if (len(product_found)>0):
        return jsonify({"product":product_found[0]})
    return jsonify({"product":"Producto no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)