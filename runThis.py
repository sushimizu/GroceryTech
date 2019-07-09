from flask import Flask , render_template


app = Flask(__name__) 



@app.route('/') 
def index():
	return render_template('login1.html')

@app.route('/registrationType')
def registrationType():
	return render_remplate('registrationType2.html')


























if __name__ == '__main__' :
	app.run(debug=True, host='0.0.0.0') 
