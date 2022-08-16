from flask import Flask, render_template, request, make_response, redirect, url_for
from socket import *
app = Flask(__name__)


def TCPCliGetList(Fromcity):
    serverName = "localhost"
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = Fromcity
    clientSocket.send(message.encode())
    modifiedmessage = clientSocket.recv(1024)
    new_mes = modifiedmessage.decode().replace("[", "")
    new_mes2 = new_mes.replace("]", "")
    new_mes3 = new_mes2.split(", ")
    clientSocket.close()
    return new_mes3






USERS=[]
btemp=TCPCliGetList("b")
bregn = TCPCliGetList("r")
oregn = TCPCliGetList("p")
print(btemp)
otemp = TCPCliGetList("o")
print(otemp)



@app.route("/index")
@app.route("/")
def index():
    username = request.cookies.get('username')
    if username:
        if username not in USERS:
            USERS.append(username)
        return render_template("menu.html", username=username)
    return render_template("registration.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    USERS.append(username)
    resp = make_response(redirect("/index"))
    resp.set_cookie('username', username)
    return resp


@app.route("/ran-pic")
def random_picture():
    return render_template("random-picture.html")


@app.route("/berTemp")
def berTemp():
    return render_template("berTemp.html", berTemp = btemp)

@app.route("/berRegn")
def berRegn():
    return render_template("berRegn.html", berRegn = bregn)

@app.route("/osloRegn")
def osloRegn():
    return render_template("osloRegn.html", osloRegn = oregn)

@app.route("/osloTemp")
def osloTemp():
    return render_template("osloTemp.html", osloTemp = otemp)


@app.route("/users")
def users():
    return render_template("users.html", users=USERS)
