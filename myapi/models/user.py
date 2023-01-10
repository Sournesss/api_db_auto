from myapi.extensions import db, pwd_context


class User(db.Model):
    """Basic user model"""
    id = db.Column(db.Integer, unique=True, primary_key=True)

    def __repr__(self):
        return f'User -> {self.id}'
