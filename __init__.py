# initializes the Flask application object

from flask import Flask

app = Flask(__name__)

# import views, models, forms, etc.
# from app import views, models, forms, etc.

if __name__ == '__main__':
    app.run()
