from Database.Models.action_type import ActionType
from Database.Models.device_type import DeviceType
from Database.connection import db


def create_action_type(device_type: DeviceType, name: str, description: str, uri: str) -> ActionType:
    new_action_type = ActionType(name, description, uri)

    db.session.add(new_action_type)
    db.session.commit()

    return new_action_type
