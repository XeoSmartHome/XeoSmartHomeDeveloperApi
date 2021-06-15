from Database.Models.device_type import DeviceType


def get_device_type_by_id(device_type_id: str) -> DeviceType:
    device_type = DeviceType.query.filter(DeviceType.id == device_type_id).first()
    if device_type is None:
        raise Exception('DeviceTypeNotFound')
    return device_type
