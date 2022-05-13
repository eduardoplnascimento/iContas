from flask import render_template

class HomeController():
    def index():
        return render_template('index.html')
    def login():
        return render_template('signin.html')
