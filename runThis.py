from flask import Flask , render_template
from flask import request


app = Flask(__name__) 



@app.route('/', methods=['GET','POST']) 
def index():
	return render_template('login1.html')


@app.route('/registrationType', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')

@app.route('/buyerFunctionality', methods=['GET','POST'])
def buyerFunctionlity():
	if request.method == 'POST':
		if validLogin(request.form['username'], request.form['password']):
			return render_template('buyerfunctionality3.html')
		else:
			error="Invalid Username/Password"
		
	return render_template('login1.html', error=error)























if __name__ == '__main__' :
	app.run(debug=True, host='0.0.0.0') 
