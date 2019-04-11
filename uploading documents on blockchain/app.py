from flask import Flask,render_template,request,jsonify
#import mysql.connector
#import json,random
app =Flask(__name__)
"""mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database="login"
	)
mycurser =mydb.cursor()
#mycurser.execute("CREATE DATABASE mydocuments")
#mycurser.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")
for x in mycurser:
  print(x)
mycurser.execute("SHOW TABLES")

for x in mycurser:
  print(x)
"""
@app.route('/upload' ,methods=['POST'])

def upload():
	#data=request.get_json()
	#result=""
	#result=data

	b = request.args.get('hash', 0)
	print(b)
	return jsonify(result=b)
	#print(data)
	#return render_template("upload.html",data=data)
	"""mycursor = mydb.cursor()

	sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
	val = ("user address", "data")
	mycursor.execute(sql, val)

	mydb.commit()

def uploadissued():
	mycursor = mydb.cursor()

	sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
	val = ("user address", "document hash")
	mycursor.execute(sql, val)

	mydb.commit()"""


@app.route('/log',methods=['GET','POST'])
def log():
        return render_template("profile.html")

@app.route('/')
def index():
        return render_template("home.html",)

if __name__ == "__main__":
	app.run()
