from sqlalchemy.orm import validates

from Database.connection import db


class DeviceType(db.Model):
    __tablename__ = 'DEVICE_TYPE'

    id = db.Column(db.Integer(), name='ID', primary_key=True, nullable=False, unique=True)

    name = db.Column(db.String(), name='NAME', nullable=False)
    description = db.Column(db.String(), name='DESCRIPTION', nullable=False)
    default_image = db.Column(db.String(), name='DEFAULT_IMAGE', nullable=False)

    def __init__(self, name, description, default_image):
        self.name = name
        self.description = description
        self.default_image = default_image

    @validates('name')
    def validate_name(self, key, name):
        return name

    @validates('description')
    def validate_description(self, key, description):
        return description

    @validates('default_image')
    def validate_default_image(self, key, default_image):
        return default_image

    def __repr__(self):
        return f'<id: {self.id},' \
               f' name: {self.name},' \
               f' description: {self.description},' \
               f' default_image: {self.default_image}>'
