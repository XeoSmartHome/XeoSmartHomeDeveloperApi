from sqlalchemy.orm import validates

from Database.connection import db


class Address(db.Model):
    __tablename__ = 'ADDRESS'

    id = db.Column(db.Integer, name='ID', primary_key=True, nullable=False, unique=True)

    country = db.Column(db.String, name='COUNTRY', nullable=False)
    state = db.Column(db.String, name='STATE', nullable=False)
    city = db.Column(db.String, name='CITY', nullable=False)
    street = db.Column(db.String, name='STREET', nullable=False)

    def __init__(self, country, state, city, street):
        self.country = country
        self.state = state
        self.city = city
        self.street = street

    @validates('country')
    def validates_country(self, key, country):
        return country

    @validates('state')
    def validate_state(self, key, state):
        return state

    @validates('city')
    def validate_city(self, key, city):
        return city

    @validates('street')
    def validate_street(self, key, street):
        return street

    def __repr__(self):
        return f'<id: {self.id},' \
               f' state: {self.state},' \
               f' city: {self.city},' \
               f' street: {self.street}>'
