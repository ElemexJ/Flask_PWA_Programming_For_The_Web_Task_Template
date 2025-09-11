from flask import Flask
from flask import render_template
from flask import request
import database.database_manager as dbHandler
import sqlite3

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/games.html", methods=["GET", "POST"])
def games():
    conn = sqlite3.connect("database/data_source.db")
    cursor = conn.cursor()
    if request.method == "POST":
        filter_term = request.form.get("filter_term", "")
        filter_category = request.form.get("category", "")
        if filter_category:
            query = "SELECT PageId, game, category, about, image FROM GamePages WHERE (game LIKE ? OR category LIKE ?) AND category = ?"
            cursor.execute(
                query, (f"%{filter_term}%", f"%{filter_term}%", filter_category)
            )
        else:
            query = "SELECT PageId, game, category, about, image FROM GamePages WHERE game LIKE ? OR category LIKE ?"
            cursor.execute(query, (f"%{filter_term}%", f"%{filter_term}%"))
        data = cursor.fetchall()
    else:
        data = dbHandler.listGames()
    conn.close()
    return render_template("/partials/games.html", content=data)


@app.route("/add.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def add():
    data = dbHandler.listExtension()
    return render_template("/partials/add.html", content=data)


@app.route("/signup.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def signup():
    data = dbHandler.listExtension()
    return render_template("/partials/signup.html", content=data)


@app.route("/about.html", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def about():
    data = dbHandler.listExtension()
    return render_template("/partials/about.html", content=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
