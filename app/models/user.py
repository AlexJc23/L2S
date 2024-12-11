from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    message = db.Column(db.String(1000), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'email': self.email,
            'message': self.message
        }
