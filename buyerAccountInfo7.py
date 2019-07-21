


tempdictionary = {
	'fname': 'John',
	'lname': 'Smith',
	'uname': 'Jsmith',
	'prefStore': 'Kroger',
	'storeAddr' : "600 McPublix Crl",
	'email': 'jsmith@gmail.com',
	'phone': '888-888-8888',
	'address': '123 north ave',
	'city': 'Atlanta',
	'state': 'Georgia',
	'zip': '30363',
	'defaultPay': 'Visa',
	'cardNo': '222222222'
}

def makeLine(name):
	s = """<input type="text" name ='' placeholder= """
	s += tempdictionary.get(name)
	s += "> <br> <br>"
	return s




def buyerAccInfo():
	top = """ <!DOCTYPE HTML> 

	<html>
		<head>
			<title>Buyer Account Information </title>
			<link rel="stylesheet" type="text/css" href="/static/style.css"/>
		</head>
	<body>


		<h2>  Buyer Account Information </h2>



		<form action="buyerAccountInfo7.html" method="post">  """


	bottom = """  <input type="submit" value="update"> <br> <br>

		</form>


			<form action="/buyerFunctionality">
		  <input type="submit" value="Back" >
			</form>

	    <form action="/">
		  <input type="submit" value="Delete Account" >
			</form>


	</body> """


	middle = """ <div class="row">
	  <div class="column"> 
	  First Name:"""
			 
	middle += makeLine('fname') 
	 
	middle += """
	  Username:"""
	middle += makeLine('uname') 
		
	middle += """
	  Preferred Grocery Store:"""
	middle += makeLine('prefStore') 
	
	middle += """
	  Store Address:"""
	middle += makeLine('storeAddr') 
	
	middle += """
	  Email:"""
	middle += makeLine('email') 
	
	middle += """
	  Preferred Card Number:"""
	middle += makeLine('cardNo') 
	
	  
	middle += """
	  Routing Number:"""
	middle += makeLine('defaultPay') 
	     
		
	middle += """
	  </div>
	  <div class="column">
	  Last Name:
			 <input type="text" name="lname"> <br> <br>
	  Phone:
			 <input type="text" name="phone"> <br> <br>
	  Address:
			 <input type="text" name="address"> <br> <br>
			City:
			 <input type="text" name="city"> <br> <br>
			State:
			 <input type="text" name="state"> <br> <br>
			ZipCode:
			 <input type="text" name="zip"> <br> <br>

	  </div>
	</div>
	"""



	text = top + middle + bottom
	return text
