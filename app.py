from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json

app = Flask(__name__)
app.secret_key = 'none'

with open(r'clipboard_data.json', 'r') as file:
    data = json.load(file)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/test")
def test():
    return jsonify(data)
