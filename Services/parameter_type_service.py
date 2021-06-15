from Database.Models.action_type import ActionType
from Database.Models.parameter_type import ParameterType
from Database.connection import db


def create_parameter_type(action_type: ActionType, name: str, description, uri: str, min_value: float, max_value: float,
                          default_value: float) -> ParameterType:
    new_parameter_type = ParameterType(name, description, uri, min_value, max_value, default_value)

    db.session.add(new_parameter_type)
    db.session.commit()

    return new_parameter_type
