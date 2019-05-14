from flask import Flask, request
from flask import render_template
import requests

# чуть гортань не порвала

URL_TO_SEND = "http://127.0.0.1:5000/jsonresult"
HEADERS = {"content-type": 'application/json'}

app = Flask(__name__)

# products = [
#     {"name": "iPhone", "price": 20000},
#     {"name": "Galaxy A8", "price": 15000},
#     {"name": "Xiaomi Mi 8", "price": 10000},
#     {"name": "Meizu P Smart", "price": 1000},
#     {"name": "iPhone", "price": 20000},
#     {"name": "Galaxy A8", "price": 15000},
#     {"name": "Xiaomi Mi 8", "price": 10000},
#     {"name": "Meizu P Smart", "price": 1000},
#     {"name": "iPhone", "price": 20000},
#     {"name": "Galaxy A8", "price": 15000},
#     {"name": "Xiaomi Mi 8", "price": 10000},
#     {"name": "Meizu P Smart", "price": 1000}
# ]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Index", products=products)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route('/result', methods=["POST"])
def result():
    formresult = request.form
    response = requests.post(URL_TO_SEND, json=formresult)
    return render_template("/result.html", result=response.json())


@app.route("/jsonresult", methods=["POST", "GET"])
def jsonresult():
    if request.method == "POST":
        return str.replace(str(request.json), '\'', '\"')


# @app.route("/jsonresult", methods=["POST", "GET"])
# def jsonresult():
#     if request.method == "POST":
#         result = request.get_json()
#         return render_template("jsonresult.html", result=result)

# @app.route("/userform", methods=["POST", "GET"])
# def userform():
#     if request.method == "POST":
#         formresult = request.form
#         # return render_template("jsonresult.html", result=formresult)
#         response = requests.post(URL_TO_SEND, json=formresult, headers=HEADERS)
#         return render_template("jsonresult.html")
#     else:
#         return render_template("form.html", url=URL_TO_SEND)
#
#
# @app.route('/form/<ind>')
# def form(ind):
#     return render_template("form.html", user=products[int(ind)])
#
#
# @app.route('/result', methods=["POST"])
# def result():
#     formresult = request.form
#     return render_template("result.html", result=formresult)
if __name__ == '__main__':
    app.run()
