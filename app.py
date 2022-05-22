from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'none'


@app.route("/")
def index():
    return render_template('index.html')
