from flask import Flask 
from flask import request 
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import pooling
from flask import jsonify

app=Flask(__name__)
app.secret_key="key"

load_dotenv()
local_password=os.getenv("password")
connectionpool=pooling.MySQLConnectionPool(pool_name="poolname",
                                            pool_size=3,
                                            pool_reset_session=True,
                                            host="localhost",
                                            port="3306",
                                            user="root",
                                            password=local_password,
                                            database="login_system")

@app.route("/")
def index():
    return render_template("page.html")

@app.route("/signup", methods=["POST"])
def signup():
    try:
        connection=connectionpool.get_connection()
        cursor=connection.cursor()
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
            cursor.execute("INSERT INTO `member` (`name`,`username`,`password`)VALUES(%s,%s,%s)",(name,username,password))
            connection.commit()
            return redirect("/")
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        connection.rollback()
    except:
        print("other error")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("connection is closed")

@app.route("/signin", methods=["POST"])
def signin():
    try:
        connection=connectionpool.get_connection()
        cursor=connection.cursor()
        username=request.form["username"]
        password=request.form["password"]
        cursor.execute("SELECT `name` FROM `member` WHERE `username`=%s and `password`=%s",(username,password))
        name=cursor.fetchone()
        if name:
            session["username"]=username
            session["name"]=name[0]
            session["login"]=True
            return redirect("/member/")
        elif username=="" or password=="":
            return redirect("/error?message=請輸入帳號、密碼")
        else:
            return redirect("/error?message=帳號或密碼輸入錯誤")
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        connection.rollback()
    except:
        print("other error")
    finally:
       if connection.is_connected():
            cursor.close()
            connection.close()
            print("connection is closed")

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
    
@app.route("/api/members")
def members():
    try:
        connection=connectionpool.get_connection()
        cursor=connection.cursor()
        username=request.args.get("username", "")
        cursor.execute("SELECT * FROM `member` WHERE `username`=%s",(username,))
        user=cursor.fetchone()
        if user:
            information={
                "data":{
                    "id":user[0],
                    "name":user[1],
                    "username":user[2]
                }
            }
            response=jsonify(information)
            return response
        else:
            information={
                "data":None
            }
            response=jsonify(information)
            return response
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        connection.rollback()
    except:
        print("other error")
    finally:
       if connection.is_connected():
            cursor.close()
            connection.close()
            print("connection is closed")

@app.route("/api/member", methods=["POST"])
def api_member():
    try:
        connection=connectionpool.get_connection()
        cursor=connection.cursor()
        data=request.get_json()
        name_update=data["name"]
        username=session["username"]
        if session["login"]==True:
            cursor.execute("UPDATE `member` SET `name`=%s WHERE `username`=%s",(name_update,username))
            connection.commit()
            information={
                "ok":True
            }
            response=jsonify(information)
            return response
        else:
            information={
                "error":True
            }
            response=jsonify(information)
            return response
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        connection.rollback()
    except:
        print("other error")
    finally:
       if connection.is_connected():
            cursor.close()
            connection.close()
            print("connection is closed")

if __name__=="__main__":
    app.run(port=3000)