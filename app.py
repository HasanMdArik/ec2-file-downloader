from flask import Flask, send_file, send_from_directory, abort

app = Flask(__name__)

app.config["dataDir"] = __file__.split(__file__.split("/")[-1])[0] + "data"


@app.route("/")
def getData():
    try:
        return send_from_directory(directory=app.config["dataDir"], filename="data.zip", as_attachment=True, path="./")
    except FileNotFoundError:
        return {"message": "zip file didn't found"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
