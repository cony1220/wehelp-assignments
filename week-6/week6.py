from flask import Flask 
from flask import request 
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
import mysql.connector

app=Flask(__name__)
app.secret_key="key"

@app.route("/")
def index():
    return render_template("page.html")

@app.route("/signup", methods=["POST"])
def signup():
    connection = mysql.connector.connect(host="localhost",
                                    port="3306",
                                    user="root",
                                    password="password",
                                    database="login_system")
    cursor = connection.cursor()
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    cursor.execute("SELECT * FROM `member` WHERE `username`=%s",[username])
    examine_username=cursor.fetchone()
    if examine_username:
        return redirect("/error?message=帳號已經被註冊")
    elif examine_username==None and password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        cursor.execute("INSERT INTO `member` VALUES(%s,%s,%s)",(name,username,password))
        connection.commit()
        return redirect("/")
    cursor.close()
    connection.close()

@app.route("/signin", methods=["POST"])
def signin():
    connection = mysql.connector.connect(host="localhost",
                                    port="3306",
                                    user="root",
                                    password="password",
                                    database="login_system")
    username=request.form["username"]
    password=request.form["password"]
    cursor = connection.cursor()
    cursor.execute("SELECT `name` FROM `member` WHERE `username`=%s and `password`=%s",(username,password))
    name=cursor.fetchone()
    if name:
        session["name"]=name[0]
        session["login"]=True
        return redirect("/member/")
    elif username=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    cursor.close()
    connection.close()

@app.route("/member/")
def member():
    user=session["name"]
    if session["login"]==True:
        return render_template("member.html", name=user)
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message", "")
    return render_template("error.html", text=message)

@app.route("/signout")
def signout():
    session["login"]=False
    return redirect("/")
    
if __name__=="__main__":
    app.run(port=3000)