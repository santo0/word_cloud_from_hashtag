from flask import Flask, render_template, url_for, request, redirect, Response
from datetime import datetime
import os
import main
import re
import sys

IMAGES_FOLDER = os.path.join('static', 'temporary_files')
TWEET_LEN = 140

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        hashtag_name = request.form['hashtag']
        splitted_hashtags = [ht.strip() for ht in re.split(", ", hashtag_name)]
        if check_if_hashtags_are_valid(splitted_hashtags):
            main.run(splitted_hashtags)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig100.png')
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