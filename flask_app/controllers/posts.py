from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.post import Post
from datetime import datetime

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/results")
def show_search_results():
    return render_template("posts.html")