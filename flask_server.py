

from flask import Flask
from flask_inertia import Inertia, render_inertia

SECRET_KEY = "alsjdfal;osudfgha;lsuehgf;alsuegha;sliegh1;lo3u5yto923yg!"
INERTIA_TEMPLATE = "base.html"

app = Flask(__name__)
app.config.from_object(__name__)

inertia = Inertia(app)


@app.route("/")
def index():
    return render_inertia("js/pages/Index", {"name": "World"})


@app.route("/test/")
def test():
    return render_inertia("js/pages/Test", {"foo": "bar"})

