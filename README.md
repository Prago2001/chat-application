# What is this?

A support chat application for a company.  

# How do I get started?
## Prerequisites
We assume you have the following installed already:
  * Python 3 [here](https://docs.python-guide.org/starting/installation/)
  * SQLlite Database - Automatically created by Django application


## Setup

  * Ensure pip is installed using `pip --version`. Ensure python version from the output is >=3.7.
  * Install virtualenv `pip install virtualenv`.
  * Clone the repo and navigate into the top-level directory.
  * Create a virtual environment (venv) for installing Python packages, then
  activate it and install all required packages:
  ```bash
  virtualenv venv
  source venv/bin/activate
  cd chat-application/
  pip install -r requirements.txt
  ```
  * Run the following commands:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
  * Populate the db with the entries from CSV file:
  ```bash
  python manage.py runscript read_csv
  ```
  * A users.txt file will get created. Refer to it while logging in.
  * The password for all users is: `branch12`
  * Finally run the server: `python manage.py runserver`.
  * 'users.txt' contains usernames of customers.
  * Login of agents: Usernames-> `agent1`,`agent2`, Password -> `branch12`