from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/tech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



from controller import *
from models import *
from extensions import *


if __name__ == '__main__':
    # app.init_app(db)
    # app.init_app(migrate)
    app.run(port=5000,debug=True)

