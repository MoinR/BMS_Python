def sendData():
	try:
		mydb = conn.connect(
	  		host="localhost",
	  		user="root",
	  		passwd="m",
			database = "bms"
		)
		statement = mydb.cursor()
		sql = "SELECT * FROM user WHERE username =" + name +" AND password = "  + password + ";";
		statement.execute(sql);
		mydb.commit(); 
		
		
	except Exception as e:
		print(e);

