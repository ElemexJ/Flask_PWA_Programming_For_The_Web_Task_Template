from flask import Flask
from flask import render_template
from flask import request
import database.database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/add.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def add():
    data = dbHandler.listExtension()
    return render_template("/partials/add.html", content=data)


@app.route("/about.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def about():
    data = dbHandler.listExtension()
    return render_template("/partials/about.html", content=data)


@app.route("/games.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def games():
    data = dbHandler.listExtension()
    return render_template("/partials/games.html", content=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
