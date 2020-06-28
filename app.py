from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os
import main

IMAGES_FOLDER = os.path.join('static', 'temporary_files')
TWEET_LEN = 140

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        hashtag_name = request.form['hashtag']
        if check_if_hashtags_are_valid(hashtag_name):
            main.run(hashtag_name)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig.png')
            return render_template("search.html", image = full_filename)
    else:
        return render_template("index.html")

def check_if_hashtags_are_valid(hashtags):
    splitted_hashtags = [ht.strip() for ht in hashtags.split(",")]
    if len(splitted_hashtags == 0):
        return False
    else:
        for ht in splitted_hashtags:
            if ht[0] != '#' or TWEET_LEN < ht.len() or ' ' in ht:
                return False
        return True

if __name__ == "__main__":
    app.run(debug=True)