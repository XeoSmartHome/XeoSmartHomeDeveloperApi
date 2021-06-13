from flask import Flask

from API import api
from Database.Models.developer import Developer
from Database.connection import db
from login_manager import login_manager

app = Flask(__name__)


login_manager.init_app(app)
db.init_app(app)


app.register_blueprint(api)


@app.route('/')
def hello_world():
    d1 = Developer('claudiu', 'neamtu', '@1', '123', 1)
    d2 = d1
    print(d2)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
