# Item Catalog : Book Store
## By Sana Sudha
This BooStore is a project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About Project:
The BookStore is an utilizing the Flask framework which accesses a SQL database that populates different types of novels and authors. Any user can view the novelitems but only authenticated people can add an item, edit an item, delete an item. Currently OAuth2 is implemented for Google Accounts.

## In This Project
This project has one main Python module `controller.py` which runs the Flask application. A SQL database is created using the `model.py` module and you can populate the database with test data using `db_init.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application.

## Requirements
* Python
* Html5
* CSS
* Flask FrameWork
* OAuth
* SQLAlchemy

## Installation Process with step-by-step 
There are some resourses and instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Resourses
- Vagrant 
- Udacity Vagrantfile 
- VirtualBox 


## How to Install

Step-1 --> Install [Python](https://www.python.org/downloads)
    
Step-2 --> Install [Vagrant](https://www.vagrantup.com/downloads.html)
    
Step-3 --> Install [VirtualBox](https://www.virtualbox.org/wiki/downloads)
    
Step-4 --> Install [Git](https://git-scm.com/download/win) --> For Windows
    
Step-5 --> Launch the vagrant virtual machine inside vagrant sub-directory then open Git Bash: `$vagrant up`
    
Step-6 --> Login to vagrant virtual machine --> `$vagrant ssh`
    
Step-7 --> Change directory to /vagrant --> `$cd /vagrant/`
    
Step-8 -->  Change directory to  Projectors project folder inside vagrant folder--> `$cd Item_Catalog`
    
Step-9 --> Install the requirement project modules are:
    
        	* `sudo pip install flask`
        	* `sudo pip install oauth2client`
        	* `sudo pip install sqlalchemy`
        	* `sudo pip install requests`
    
Step-9 --> Create application database:`$python model.py`
    
Step-10 --> Inserting application data in database -->`$python db_init.py`

Step-11 --> Run the main project file -->`python controller.py`
    
Step-12 --> Access the application any local browser[http://localhost:5000](http://localhost:5000)

* Optional step(s)

## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Book-Store'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in book-store directory that you cloned from here
14. Run application using `python /book-store/controller.py`

## JSON Endpoints
The following are open to the public:

Books Catalog JSON: `/BookStore/JSON`
    - Displays the Novel books catalog. Book Categories and authors.

Book Categories JSON: `/bookStore/bookCategories/JSON`
    - Displays all book categories

Book Item Details JSON: `/bookStore/bookItems/JSON`
	- Displays book items

## Miscellaneous

This project is inspiration from [SkBadulla](https://github.com/SkBadulla/Item_Catalog).



