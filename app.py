from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import main

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        hashtag_name = request.form['hashtag']
        main.get_tweets(hashtag_name)
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)