from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("dashboard.html")

@main.route('/login')
def login():
    return "<h2>Login page coming next...</h2>"
