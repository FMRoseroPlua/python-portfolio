from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import json

app = Flask(__name__)
bootstrap = Bootstrap5(app)

with open('./tmp/projects.json', 'r', encoding='utf-8') as file:
    my_projects = json.load(file)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html", projects=my_projects)


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()


#uv run flask --app app run --debug


