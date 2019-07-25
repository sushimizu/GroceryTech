# GroceryTech
CS 4400 project 

RUNNING THE WEB APP:


    If you don't already have them, install Python 3.7, pip, mySQL Server and mySQL Workbench.

    Clone the repository to your computer. You can find this repository at https://github.com/sushimizu/GroceryTech . These instructions will assume you cloned it to a directory called GroceryTech.
    
    Look at line 6 from db.py, ensure that the password on that file is the password (passwd) you use to acces your local host root in mysql workbench.

    Run GroceryTech.sql to setup and add starter data to the database.

    You can access the application at (127.0.0.1:5000) or (localhost:5000).

    Sign in with the following credentials, or create your own account. Note that there are a variety of populated users to enter in as:

    buyer: adepttimberry / cakeholmium

    deliverer: chivalrouspotatoes / clamcarbon

    Manager: ciscocobalt / santandercesium

PROJECT STRUCTURE:
    This repository contains 3 main things:

    SQL files for setting up the database
    Python with Flask and pymySQL addons (backend) files
    HTML (frontend) files

Prerequisites to run the webserver:

    Make sure you have all of the dependencies (see Installing the dependencies, below)

INSTALLING THE DEPENDENCIES:


    Make sure you have googleChrome or Safari on your computer, if not download it from your web browser.
    Make sure you have Python3.7 64 bits, if you don't have it,  go to https://www.python.org/ and install python3
    
    Make sure you have installed Mysql Workbench, Mysql server, and Mysql connectors. If you dont have it, go to https://dev.mysql.com/downloads/installer/, and install everything as recommended. Make sure to remember the password for your server. You must then go to line 6 in db.py and change the password to your SQL server's password.
    
    Open a shell (Terminal or Command Prompt), enter the directory and run pip install -r requirements.txt to the needed python modules not already installed on python.
    
    If after running any code, if any library is missing, type in the command prompt under the directory in which python is installed  "pip install" plus the name of the library
    
    

WHAT'S WHERE:


    runThis.py contains all of the HTML routes. That is, this is where the connections between every page on the website are defined.
    Some of the functions in runThis.py are organized into db.py to keep everything organized. We tried to keep most of the actual database queries in the db.py file.
    Templates contains the actual HTML used. There is one HTML page for every distinct page on the website. 
    GroceryTech.sql contains the  sql code to create our database schema and populate it with values.


TO RUN:
To use, run in terminal:

$ python runThis.py

or 

$ python3 runThis.py

then paste the provided link (usually http://127.0.0.1:5000) into browser. If link is different to what is given in the terminal upon running runThis.py, defer to the link in the terminal.
