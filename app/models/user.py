from beanie import Document


class User(Document):
    first_Name: str
    last_name: str
    email: str
    password: str
