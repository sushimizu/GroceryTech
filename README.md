# GroceryTech
CS 4400 project 

RUNNING THE WEB APP:


    If you don't already have them, install Python 3 and pip.

    Clone this repository to your computer. These instructions will assume you clone it to a directory called trip-planner.

    Switch to the trip-planner directory.

    Create a virtual environment to contain this project. The way you do this will vary depending on your operating system:

    a. Windows: Run py -3 -m venv venv

    b. Mac: Run python3 -m venv venv

    Activate the virtual environment. Run the appropriate command for your OS:

    a. Windows: Run venv\Scripts\activate

    b. Mac: Run . venv/bin/activate

    Look for a (venv) at the beginning of each new line in your terminal. This means you're in your virtual environment.

    Run pip install -r requirements.txt to install the dependencies.

    Copy the .env.example file to .env and add the required values by following the directions in the files.

    Run team11-schema.sql and team11-data.sql to setup and add starter data to the database.

    Start the webserver by running flask run inside the virtual environment.

    You can access the application at 127.0.0.1:5000 or localhost:5000.

    Sign in with the following credentials, or create your own account:

buyer: admin@example.com / password

deliverer: someone@example.com / password

Manager:

PROJECT STRUCTURE:
This repository contains 3 main things:

    SQL files for setting up the database
    Flask server (backend) files
    HTML (frontend) files

Prerequisites to run the webserver:

    Make sure you have all of the dependencies (see Installing the dependencies, below)

INSTALLING THE DEPENDENCIES:


    Make sure you have googleChrome or Safary on your computer, if not downlowad it from your web browser.
    Make sure you have Python3 64 bites, if you don't have it,  go to https://www.python.org/ and istall python3
    
    Make sure you have installed Mysql Workbench, Mysql server, and Mysql connectors. If you dont have it, go to https://dev.mysql.com/downloads/installer/, and install everything as recommended. Make sure to remember the password for your server.
    
    Open a shell (Terminal or Command Prompt), enter the directory and run pip install -r requirements.txt to install Flaskif flask is not already installed on python.
    
    If after running any code, if any library is misssing, type in the command promt under the directory in which python is installed  "pip install" plus the name of the library
    
    

WHAT'S WHERE:


    runThis.py contains all of the HTTP routes. That is, this is where what happens when you visit every page on the website is defined.
    Some of the functions in runThis.py are organized into db.py to keep everything organized.
    templates contains the actual HTML used. There is none HTML page for every distinct page on the website. 
    GroceryTech.sql contains the  sql code to create our database schema and insert values into it.


TO RUN:
To use, run in terminal:

$ python runThis.py

or 

$ python3 runThis.py

then paste the provided link (http://0.0.0.0:5000) into browser
