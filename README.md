# SE-Lite-Scrum
This is the final project in `Software Engineering` Course in the 
[Open University of Israel](https://www.openu.ac.il/en/pages/default.aspx)[CS 22916]  
The Project is project management system that implement most of Scrum methodology
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.   

## Installing instruction
* Clone the repository from GitHub
* Install python 3.5 or higher
* it is recommended to create a virtual environment for the current project:

```
Create a virtual environment  
	virtualenv <env name>  
Activate the virtual environment  
	activate <env name>  
```
* Install requires module using the requirement file:
We need to import needed modules that are the building blocks of the project, for that, I have created a requirements file named: requirements.txt to install all modules you need to run the following command line in the project directory: 
	pip install -r requirements.txt
* run the server by entering to the address that will appear, usually, it will be `http://127.0.0.1:8000`  

### Sample data and how to start a fresh clean system
the cloned project includes code, database and sample data. The superuser username is `user` and password is `test1234`
#### Clear sample data
To get a clean system you need to follow these steps:
1.	Delete the db.sqlite file.
2.	Run the run.bat 
3.	you need to fiil the superuser information at the end of the batch.

> This batch run in 3 steps:
> *	`python manage.py makemigrations <app-name by folder>` for every app folder
> *	`python manage.py migrate` 
> *	`python manage.py createsuperuser`


# GETTING STARTED  
the first page we see is:
![image](https://user-images.githubusercontent.com/12948709/33794506-19e84aee-dcd6-11e7-96e1-acda7d6dbf4c.png)  
we can login using our superuser account  
or we can register a new user.
## main workflow
in a new system we need:
1. add new user to the system
>we create a users pool for all companies and projects.
2. create a company
3. create a groups to the comapny  
3.1 add users to the gorup
> automatically the system creates a group (named as the company), this is for to group all company users together

## create a project



