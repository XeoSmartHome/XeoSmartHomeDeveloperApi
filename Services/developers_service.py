from Database.Models.developer import Developer
from Database.connection import db


def create_developer(first_name: str, last_name: str, email_address: str, password: str, phone_number: str) -> Developer:
    new_developer = Developer(first_name, last_name, email_address, password, phone_number)

    db.session.add(new_developer)
    db.session.commit()

    return new_developer
