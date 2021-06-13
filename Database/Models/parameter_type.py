from sqlalchemy.orm import validates

from Database.connection import db


class ParameterType(db.Model):
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)

    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    uri = db.Column(db.String(), nullable=False)

    min_value = db.Column(db.Float(), nullable=False)
    max_value = db.Column(db.Float(), nullable=False)
    default_value = db.Column(db.Float(), nullable=False)

    def __init__(self, name, description, uri, min_value, max_value, default_value):
        self.name = name
        self.description = description
        self.uri = uri
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value

    @validates('name')
    def validate_name(self, key, name):
        return name

    @validates('description')
    def validate_description(self, key, description):
        return description

    @validates('uri')
    def validate_default_uri(self, key, uri):
        return uri

    @validates('min_value')
    def validate_min_value(self, key, min_value):
        return min_value

    @validates('max_value')
    def validate_max_value(self, key, max_value):
        return max_value

    @validates('default_value')
    def validate_default_value(self, key, default_value):
        return default_value
