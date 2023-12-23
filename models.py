class Product:
    def __init__(self, id, name, description, price, category, userId):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.userId = userId

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'userId': self.userId
        }


class User:
    def __init__(self, id, name, email, password, userType):
        self.id = id
        self.name = name
        self.email = email
        self.password = password  # Note: In a real application, never store plain passwords!
        self.userType = userType

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'userType': self.userType
        }
