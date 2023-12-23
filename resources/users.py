from flask_restful import Resource, reqparse

# In-memory storage for users
USERS = []

# Parser for user data
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)
user_parser.add_argument('userType', type=str, required=True, choices=('buyer', 'seller', 'both'))

class UserRegister(Resource):
    def post(self):
        """Register a new user."""
        data = user_parser.parse_args()
        if any(user['email'] == data['email'] for user in USERS):
            return {'message': 'A user with that email already exists'}, 400

        new_user = {
            'id': len(USERS) + 1,
            'name': data['name'],
            'email': data['email'],
            'password': data['password'],  # In a real app, ensure this is hashed
            'userType': data['userType']
        }
        USERS.append(new_user)
        return {"message": "User created successfully."}, 201
