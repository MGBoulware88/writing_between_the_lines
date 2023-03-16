from flask_app.models.user import User
from flask_app.models.post import Post
from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
secret_key = "CHANGEME"