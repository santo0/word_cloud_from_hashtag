from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os
import main
import re
import sys

IMAGES_FOLDER = os.path.join('static', 'temporary_files')
TWEET_LEN = 140

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        hashtag_name = request.form['hashtag']
        splitted_hashtags = [ht.strip() for ht in re.split(", ", hashtag_name)]
        if check_if_hashtags_are_valid(splitted_hashtags):
            main.run(splitted_hashtags)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig.png')
            return render_template("search.html", image = full_filename)
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")

def check_if_hashtags_are_valid(hashtags):
    if len(hashtags) == 0:
        return False
    else:
        for ht in hashtags:
            if not (0 < len(ht) <= TWEET_LEN) or ht[0] != '#':
                return False
        return True

if __name__ == "__main__":
    app.run(debug=True)