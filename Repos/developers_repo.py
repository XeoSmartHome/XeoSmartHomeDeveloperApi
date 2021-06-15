from Database.Models.developer import Developer


def get_developer_by_email(email_address: str) -> Developer:
    developer = Developer.query.filter(Developer.email_address == email_address).first()

    if developer is None:
        raise Exception('DeveloperNotFound')

    return developer


def get_developer_by_id(developer_id: int) -> Developer:
    developer = Developer.query.get(developer_id)

    if developer is None:
        raise Exception('DeveloperNotFound')

    return developer
