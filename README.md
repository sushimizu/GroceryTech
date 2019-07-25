# GroceryTech
CS 4400 project 

RUNNING THE WEB APP:


    If you don't already have them, install Python 3, pip, mySQL Server and mySQL Workbench.

    Clone this repository to your computer. You can find this repository at https://github.com/sushimizu/GroceryTech . These instructions will assume you clone it to a directory called GroceryTech.

    Run pip install -r requirements.txt to install the dependencies.

    Run GroceryTech.sql to setup and add starter data to the database.

    Start the webserver by running:
    python runThis.py

    Visit the web app at the URL listed or localhost:5000

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


    Make sure you have Python 3

    Open a shell (Terminal or Command Prompt) and navigate to the trip-planner directory

    Create a virtual environment to contain this project. The way you do this will vary depending on your operating system:

    a. Windows: Run py -3 -m venv venv

    b. Mac: Run python3 -m venv venv

    Every time you want to work with Python in this project, you need to activate the virtual environment. Run the appropriate command for your OS:

    a. Windows: Run venv\Scripts\activate

    b. Mac: Run . venv/bin/activate

    Look for a (venv) at the beginning of each new line in your terminal. This means you're in your virtual environment.

    Run pip install -r requirements.txt to install Flask and the other required Python packages.

WHAT'S WHERE:


    planner.py contains all of the HTTP routes. That is, this is where what happens when you visit every page on the website is defined.
    Some of the functions in planner.py are organized into auth.py and util.py to keep everything organized.
    templates contains the actual HTML used. Note that there isn't one HTML page for every distinct page on the website. Instead, a templating engine called Jinja is used. This reduces repetition of boilerplate code such as the navigation bar.
    templates/include includes some of the HTML foundations used by other pages.


TO RUN:
To use, run in terminal:

$ python runThis.py

or 

$ python3 runThis.py

then paste the provided link (http://0.0.0.0:5000) into browser
