from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import os
import main

IMAGES_FOLDER = os.path.join('static', 'temporary_files')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER

@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        hashtag_name = request.form['hashtag']
        main.run(hashtag_name)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'fig.png')
        return render_template("search.html", image = full_filename)
        
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port=5001)