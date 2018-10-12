import os
import json
from flask import Flask, send_from_directory
from flask_assets import Environment, Bundle

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = os.urandom(24)

@app.route("/res/<path:filename>")
def serve_res(filename):
    return send_from_directory("res", filename)

@app.route("/")
def index():
    return "You are not authorized to access this api."

@app.route("/adduser")
def db_add_record():
    # add db record
    return "" 

@app.route("/deleteuser")
def db_del_record():
    # delete db record
    return ""

@app.route("/getscores")
def get_score():
    # get user scores
    return ""

@app.route("/getfriends")
def get_friends():
    # get user friends
    return ""

@app.route("/get_leaderboard")
def get_friends_scores():
    # gets the user leaderboard
    return ""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True) # turn debug off for production!