class User:
    def __init__(self, username, email, address, city, state, zip_code):
        self.username = username
        self.email = email
        self.address = {
             "address": self.address,
             "city": self.city,
             "state": self.state,
             "zip_code": self.zip_code}