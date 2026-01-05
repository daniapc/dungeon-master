from flask import Flask
from flask.views import MethodView
# https://flask.palletsprojects.com/en/stable/views/

app = Flask(__name__)

class Jeu(MethodView):
    def __init__(self):
        pass

    def get(self):
        return "<p>Hello, World!</p>"

app.add_url_rule("/", view_func=Jeu.as_view("jeu"))

if __name__ == "__main__":
    app.run(debug=True)
    