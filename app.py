from flask import Flask
from flask_restful import Api
from resources.products import ProductList, Product
from resources.users import UserRegister
from resources.categories import CategoryList

app = Flask(__name__)
api = Api(app)

# Adding resources to the API with their corresponding routes
api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<int:product_id>')
api.add_resource(UserRegister, '/users/register')
api.add_resource(CategoryList, '/categories')

if __name__ == '__main__':
    app.run(debug=True)
