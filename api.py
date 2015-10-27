from flask import *
import json
import mysql.connector

app = Flask(__name__)

def return_json(str1,str2):
	return '{ "' + str1 + '": "' + str2 + '"}'

@app.route("/push", methods=['GET', 'POST'])
def push():
	if not request.method == "POST":
		return return_json("error", "This should be POST request")

	data = json.loads(request.data)
	return return_json("status", "200 OK"), 200



@app.route("/register/", methods=['GET', 'POST'])
@app.route("/register/<user>", methods=['GET', 'POST'])
def register(user=None):
	# mysql zajebancija
	print "Starting MySql connection"
	cnx = mysql.connector.connect(user='root', password='toor', host='127.0.0.1', database='glms') 
	cursor = cnx.cursor()
	# proverava zahtev da li je post
	if not request.method == "POST":
		return return_json("error", "This should be POST request")
	# proverava da li username valja
	if user == None:
		return return_json("error", "Parameter <user> not found in URL")
	if not isinstance(s, user):
		return return_json("error", "Something is wrong with your username")
	if 
	# proverava da li username postoji u bazi
	if not cursor.execute("SELECT user FROM users WHERE user='" + user + "'"):
		return return_json("error", "User not exist")
	json_data= request.form['data']
	data = json.loads(json_data)
	# get data from json
	try:
		nuid = data["nuid"]
		ip = request.remote_addr
		cpu = data["cpu"]
		cpucores = data["cpucores"]
		arch = data["arch"]
		kernel = data["kernel"]
		hostname = data["hostname"]
		ramtotal = data["ramtotal"]
		disktotal = data["disktotal"]
		if not cursor.execute("INSERT INTO nodes (nuid, ip, cpu, cpucores, arch, kernel, hostname, ramtotal, disktotal, user) VALUES ('" + nuid + "', '" + ip + "', '" + cpu + "', '" + cpucores + "', '" + arch + "', '" + kernel + "', '" + hostname + "', '" + ramtotal + "', '" + disktotal + "', '" + user + "');"): 
			return return_json("error", "SQL Query died while registering"), 403
	except:
		return return_json("error", "Could not parse JSON"), 403

	return return_json("status", "200 OK"), 200

	#cursor.execute("select * from node;")
	print "Closing MySql connection"
	cnx.close()
	
@app.route("/")
def index():
    return 'This is API. You can find <a href="/docu">documentation</a> here.'

@app.errorhandler(404)
def not_found(error):
    return return_json("error", "Error 404, karma is bitch"), 404



if __name__ == "__main__":
    app.run(debug=True)
