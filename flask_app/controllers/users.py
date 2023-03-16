from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")