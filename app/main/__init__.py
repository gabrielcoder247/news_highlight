from flask import Flask
from config import DevConfig

#Initialize application

app = Flask(__name__,instance_relative_config = True)

#setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

# @app.route('/')
# def index():
#     return '<h1>Hello World</h1>'


# if __name__ == '__main__':
#     app.run(debug = True)