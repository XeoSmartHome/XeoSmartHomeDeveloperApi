import datetime
import hashlib

from flask import current_app
from flask_login import UserMixin
from sqlalchemy.orm import validates, Query

from Database.connection import db


def hash_password(password: str) -> str:
    return hashlib.md5((password + current_app.config['PASSWORD_SALT']).encode('utf-8')).hexdigest()


class Developer(db.Model, UserMixin):
    __tablename__ = 'DEVELOPER'
    query: Query

    id = db.Column(db.Integer(), name='ID', primary_key=True, nullable=False, unique=True)

    first_name = db.Column(db.String(), name='FIRST_NAME', nullable=False)
    last_name = db.Column(db.String(), name='LAST_NAME', nullable=False)

    email_address = db.Column(db.String(), name='EMAIL_ADDRESS', nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(), name='PASSWORD_HASH', nullable=False)

    phone_number = db.Column(db.String(), name='PHONE_NUMBER', nullable=False)

    registered_on = db.Column(db.DateTime(), name='REGISTERED_ON', nullable=False)

    def __init__(self, first_name: str, last_name: str, email_address: str, password: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password_hash = hash_password(password)
        self.phone_number = phone_number
        self.registered_on = datetime.datetime.now()

    @validates('first_name')
    def validate_first_name(self, key, first_name):
        assert len(first_name) != 0, 'first name can not be null'
        return first_name

    @validates('last_name')
    def validate_last_name(self, key, last_name):
        assert len(last_name) != 0, 'last name can not be null'
        return last_name

    @validates('email_address')
    def validate_email(self, key, address):
        assert len(address) != 0, 'Address can not be null'
        assert '@' in address, '@ not found'
        return address

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        return phone_number

    def check_password(self, password: str) -> bool:
        return self.password_hash == hash_password(password)

    def __repr__(self):
        return f'<id: {self.id},' \
               f' first_name: {self.first_name},' \
               f' last_name: {self.last_name},' \
               f' email_address: {self.email_address},' \
               f' phone_number: {self.phone_number}>'
