import os
import json
import requests
from flask import Flask, send_from_directory, session, Response, request
from flask_assets import Environment, Bundle
import logging

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

@app.route("/getscore")
def get_score():
    # get user score
    if request.form["uuid"] and request.form["token"] and request.form["secret"]:
        if request.form["secret"] == "HIBHAVESH!":
            # retrieve user score from database
            return Response(200)
        else:
            return Response("403 Not Authorized. Secret is wrong.", 403)
    else:
        return Response("Parameters not supplied", 200)

@app.route("/getfriends", methods=["GET", "POST"])
def get_friends():
    # get user friends
    if request.method == "POST":
        if request.form["uuid"] and request.form["token"] and request.form["secret"]:
            if request.form["secret"] == "HIBHAVESH!":
                # retrieve user friends
                friends = requests.post("https://graph.facebook.com/v3.1/"+request.form["uuid"]+"/friends", data={'user-access-token':request.form["token"]})
                app.logger.info(friends.text)
                data = json.load(friends.text)
                return Response(data, 200, mimetype="application/json")
            else:
                return Response("403 Not Authorized. Secret is wrong.", 403)
        else:
            return Response("Parameters not supplied", 200)
    else:
        return "Method Not Allowed"

@app.route("/getleaderboard")
def get_friends_scores():
    # gets the user leaderboard
    return ""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True) # turn debug off for production!