import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5

from data.data import projects as my_projects

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)
load_dotenv()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html", projects=my_projects)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        smtp_sendmail(name, email, message)
        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


def smtp_sendmail(name, email, message):
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = f"New contact message from {name}"
    msg["From"] = SMTP_USER
    msg["To"] = os.getenv("CONTACT_EMAIL")
    msg["Reply-To"] = email

    msg.set_content(
        f"""
            New message from your portfolio.
        
            Name: {name}
            Email: {email}
        
            Message:
            {message}
        """
    )

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            smtp.send_message(msg)

    except Exception as e:
        print("connection error.", e)
    else:
        print("E-Mail sent successfully.")


if __name__ == "__main__":
    app.run()


# uv run flask --app app run --debug
