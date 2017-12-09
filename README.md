# SE-scrum-plus
### Installing instruction
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
We need to import needed modules that are the building blocks of the project, for that I have created a requirements file named: requirements.txt to install all modules you need to run the following command line in the project directory: 
	pip install -r requirements.txt
* run the server by entering to the address that wiil appear, useealy it will be `http://127.0.0.1:8000`  

### Sample data and how to start a fresh clean system
the cloned project includes code, database and sample data. The super user username is `user` and passworf is `test1234`
#### Clear sample data
To get a clean system you need to follow these steps:
1.	Delete the db.sqlite file.
2.	Run the run.bat 
This batch run in 3 steps:
*	`python manage.py makemigrations <app-name by folder>` for every app folder
*	`python manage.py migrate` 
*	`python manage.py createsuperuser`
