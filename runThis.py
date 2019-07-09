from flask import Flask , render_template


app = Flask(__name__) 



@app.route('/', methods=['GET','POST']) 
def index():
	return render_template('login1.html')


@app.route('/registrationType2', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')

























if __name__ == '__main__' :
	app.run(debug=True, host='0.0.0.0') 
