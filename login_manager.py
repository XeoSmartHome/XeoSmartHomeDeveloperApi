from flask_login import LoginManager


login_manager = LoginManager()


@login_manager.user_loader
def _login_manager_user_loader():
    return 0
