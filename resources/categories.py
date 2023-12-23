from flask_restful import Resource

# Example in-memory storage for categories
CATEGORIES = ["Electronics", "Furniture", "Clothing", "Books", "Vehicles", "Sports"]

class CategoryList(Resource):
    def get(self):
        """Return a list of all product categories."""
        return {'categories': CATEGORIES}, 200

# Add more category-related resources here if needed.
