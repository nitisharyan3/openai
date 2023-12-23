from flask_restful import Resource, reqparse

# In-memory storage for products
PRODUCTS = []

# Parser for product data
product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True, help="Name cannot be blank")
product_parser.add_argument('description', type=str, required=True)
product_parser.add_argument('price', type=float, required=True)
product_parser.add_argument('category', type=str, required=True)
product_parser.add_argument('userId', type=str, required=True)

class ProductList(Resource):
    def get(self):
        """Return a list of all products."""
        return {'products': PRODUCTS}, 200

    def post(self):
        """Add a new product."""
        data = product_parser.parse_args()
        new_product = {
            'id': len(PRODUCTS) + 1,
            'name': data['name'],
            'description': data['description'],
            'price': data['price'],
            'category': data['category'],
            'userId': data['userId']
        }
        PRODUCTS.append(new_product)
        return new_product, 201

class Product(Resource):
    def get(self, product_id):
        """Return details of a specific product."""
        product = next((prod for prod in PRODUCTS if prod['id'] == product_id), None)
        if product:
            return product, 200
        return {'message': 'Product not found'}, 404
