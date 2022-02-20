from flask import Flask

from routes.v1.user import user_bp

app = Flask(__name__)


@app.route('/', methods=["GET"])
def approute():
    return "ready"

app.register_blueprint(user_bp, url_prefix="/v1/users")

app.run(host="0.0.0.0", port=27032)