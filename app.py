from flask import Flask, jsonify

app = Flask(__name__)

inventory = {
    "maize flour": {"price": 2800, "stock": 120},
    "rice": {"price": 4500, "stock": 200},
    "cooking oil": {"price": 1800, "stock": 45},
}


@app.route("/")
def home():
    return jsonify({"message": "Kamau Stores API is running."})


@app.route("/api/products")
@app.route("/products")
def get_products():
    return jsonify(inventory)


@app.route("/api/products/<product_name>")
@app.route("/products/<product_name>")
def get_product(product_name):
    normalized_name = product_name.lower()
    product = inventory.get(normalized_name)
    if product is None:
        return jsonify({"error": f"Product '{product_name}' not found"}), 404
    return jsonify({"name": normalized_name, **product})


if __name__ == "__main__":
    app.run(debug=True)