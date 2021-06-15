from Database.Models.developer import Developer
from Database.Models.device_type import DeviceType
from Database.connection import db


def create_device_type(developer: Developer, name: str, description: str, default_image: str) -> DeviceType:
    new_device_type = DeviceType(name, description, default_image)

    db.session.add(new_device_type)
    db.session.commit()

    return new_device_type
