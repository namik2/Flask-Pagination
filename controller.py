from flask import render_template
from app import app
from extensions import db
from models import Blogs

@app.route("/")
def home():
    blogs = Blogs.query.all()
    return render_template('index.html', blogs=blogs)