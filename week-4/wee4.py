from flask import Flask 
from flask import request 
from flask import redirect
from flask import render_template
from flask import session
app=Flask(__name__)
app.secret_key="key"

@app.route("/")
def index():
    return render_template("page.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test":
        session["login"]="Y"
        return redirect("/member/")
    elif account=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼錯誤")

@app.route("/member/")
def member():
    if session["login"]=="Y":
        return render_template("member.html")
    else:
        return redirect("/")
@app.route("/error")
def error():
    message=request.args.get("message", "")
    return render_template("error.html", text=message)

@app.route("/signout")
def signout():
    session["login"]="N"
    return redirect("/")

app.run(port=3000)