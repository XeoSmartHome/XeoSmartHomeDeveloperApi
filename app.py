from flask import Flask

from API import api
from Config.development_config import DevelopmentConfig
from Database.Models.developer import Developer
from Database.connection import db
from login_manager import login_manager

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

login_manager.init_app(app)
db.init_app(app)

app.register_blueprint(api)


@app.route('/')
def hello_world():
    return 'XeoSmartHome Developer API'

# with app.app_context():
#    db.create_all()

if __name__ == '__main__':
    print('ok')
    app.run()
