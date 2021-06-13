from sqlalchemy.orm import validates

from Database.connection import db


class ActionType(db.Model):
    __tablename__ = 'ACTION_TYPE'

    id = db.Column(db.Integer(), name='ID', primary_key=True, nullable=False, unique=True)

    name = db.Column(db.String(), name='NAME', nullable=False)
    description = db.Column(db.String(), name='DESCRIPTION', nullable=False)
    uri = db.Column(db.String(), name='URI', nullable=False)

    def __init__(self, name, description, uri):
        self.name = name
        self.description = description
        self.uri = uri

    @validates('name')
    def validate_name(self, key, name):
        return name

    @validates('description')
    def validate_description(self, key, description):
        return description

    @validates('uri')
    def validate_default_uri(self, key, uri):
        return uri
