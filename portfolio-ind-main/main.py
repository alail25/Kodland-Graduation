from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedback.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, email, text):
        self.email = email
        self.text = text

@app.route("/", methods=["GET", "POST"])
def index():
    selected_skill = None

    if request.method == "POST":
        selected_skill = request.form.get("skill")

    return render_template("index.html", selected_skill=selected_skill)

@app.route("/form_create", methods=["POST"])
def form_create():
    email = request.form.get("email")
    text = request.form.get("text")

    if email and text:
        card = Card(email=email, text=text)
        db.session.add(card)
        db.session.commit()

    return redirect(url_for("index") + "#feedback")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)