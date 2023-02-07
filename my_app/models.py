from my_app import db

class Query_Model(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)


    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f"The name: is {self.name}, The Email is {self.email}, The message is {self.message}"



