from flask import Flask, render_template, request, url_for, session, redirect, flash
import pymysql
app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/")
@app.route('/home.html')
def home():
	return render_template('home.html')

@app.route('/venue.html')
def venue():
	return render_template("venue.html")

@app.route('/information.html')
def information():
	return render_template("information.html")

@app.route('/pictures.html')
def pictures():
	return render_template("pictures.html")

@app.route('/reservation.html')
def reservation():
	return render_template("reservation.html")

@app.route('/login.html')
def login1():
	return render_template("login.html")

@app.route('/book.html')
def book():
	return render_template("book.html")

@app.route('/register.html')
def register():
	return render_template("register.html")

@app.route('/test.html')
def reservation1():
	return render_template("test.html")


@app.route('/base.html')
def base():
	return render_template("base.html")


@app.route('/signUp_Done.html')
def signUp_Done():
	return render_template("signUp_Done.html")





db = pymysql.connect("localhost","jacky443811","jacky56220815","login")


@app.route("/login_Done.html")
def login_Done():
    if 'email' in session:
        return 'Logged in as ' + session['email'] + '<br>' + "<a href = '/logout'>Click here to log out</a>"
    else:   
        return "Hello 205CDE Class! You are not logged in <br><a href = 'login.html'>Click here to log in</a>"



@app.route("/login.html", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Execute the SQL command
        sql = ("SELECT email, password FROM Member WHERE email = '"+email+"'")
        cursor.execute(sql)

        # Commit your changes in the database
        db.commit()
        results = cursor.fetchall()
        for row in results:
            custName = row[0]
            custPassword = row[1]
            #rint ("Customer Name = %s, Password = %s" %(custName, custPassword))

            session['email'] = custName
            #return redirect(url_for('/'))

            return render_template("login_Done.html")

    return render_template("loginfail.html")
    db.close()


@app.route("/logout")
def logout():
    #remove the username from the session if it is there
    session.pop('email', None)
    return "You've logged out. Please log in again!<a href = '/login.html'>Click here to log in</a>"







@app.route('/register.html', methods=["POST","GET"])
def signup():
	if request.method =="POST":
		fname = request.form["firstname"]
		lname = request.form["lastname"]
		email = request.form["email"]
		pwd = request.form["password"]
		


		cursor = db.cursor()
		cursor.execute("""insert into Member(firstname,lastname,email,password) values(%s, %s, %s, %s)""",(fname,lname,email,pwd))


		try:
			db.commit();
			msg = "Name is sucessfully inserted"
		except Exception as e:
			db.rollback();

		return render_template("signUp_Done.html",msg = msg)
		db.close()






@app.route('/book.html', methods=["POST","GET"])
def booking():
	if request.method =="POST":
		email = request.form["email"]
		password = request.form["password"]
		phonenumber = request.form["phonenumber"]
		rooms = request.form["rooms"]
		start = request.form["starttime"]
		end = request.form["endtime"]
		people = request.form["people"]
		date = request.form["date"]
		boardgames = request.form["groupOfDefaultRadios"]
		


		cursor = db.cursor()
		cursor.execute("""insert into booking(email,password,phonenumber,rooms,starttime,endtime,people,date,boardgames) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)""",(email,password,phonenumber,rooms,start,end,people,date,boardgames))

		try:
			db.commit();
			
		except Exception as e:
			db.rollback();


		return render_template("book_Done.html")
		db.close()











if __name__ == '__main__':
    app.run(debug = True)
