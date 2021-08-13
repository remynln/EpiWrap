import os
from flask import Flask
from src import formater, intra

api = Flask(__name__)


def main():
    try:
        api.register_blueprint(intra.intra)
        print(api.url_map)
        api.run(port=8080, host="0.0.0.0", threaded=True)
    except Exception as e:
        print(e)


@api.route("/")
def root():
    return formater.response({"root": "/v1/intra",
                              "profile": "/v1/intra/profile",
                              "planning": "/v1/intra/planning"}, 200)


if __name__ == "__main__":
    main()
