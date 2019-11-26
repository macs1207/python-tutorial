from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        data = request.args.get("data")
        return "GET, {}".format(data)
    elif request.method == "POST":
        data = request.values['data']
        return "POST, {}".format(data)

if __name__ == '__main__':
    app.run(port=8080)
