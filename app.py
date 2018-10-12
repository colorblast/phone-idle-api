import os
from flask import Flask, render_template, send_from_directory
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
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True) # turn debug off for production!