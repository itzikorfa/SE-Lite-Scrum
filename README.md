# SE-Lite-Scrum
This is the final project in `Software Engineering` Course in the 
[Open University of Israel](https://www.openu.ac.il/en/pages/default.aspx)[CS 22916]  
The Project is project management system that implements most of Scrum methodology
## Getting Started
These instructions will get you a copy of the project up and run on your local machine for development and testing purposes.   

## Deployment
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
3.	you need to fill the superuser information at the end of the batch.

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
1. add a new user to the system
>we create a users pool for all companies and projects.
2. create a company
3. create groups to the company  
3.1 add users to the group
> automatically the system creates a group (named as the company), this is for to group all company users together

## create a project
### create a project workflow
1. in the company information click on create project
2. add the name of the project and description and submit
3. click on assign backlog and fill the fields in the form.
4. click on backlog setting set the length of a sprint and a template name.
> the system automatically creates the sprints backlog in the background  

![image](https://user-images.githubusercontent.com/12948709/33794971-e5114cd6-dcde-11e7-9017-d1bf97e2faf8.png)
at the end of the stages we can create a task via the create task or via sprint view.


## create a Task
### manage Task workflow  

1. there are 2 ways to add Task:  
1.1 from project view  
1.2 from sprint view   

2. the task definition includes 2 stages:  
2.1 define task user story and team  
2.2 assign task to use and sprint  

### Monitor Task
we can add a log to log ower work, the log helps to monitor how much work time has been spent and 
when the task is finished.

from the task view, we can change the stage the task is in, this operation creates a log automatically.

## Create TO-DO
To-do is a spiecel task that it is not belong to a project but belong to a user.
the todo also has a log to monitor the progress.

# All the Tasks can be view from diffrent location: 
```
User task can be viweded from the user information page
Group Tasks can be viewed  from the group information page
Sprint Tasks Can be viweed from the sprint information page
```

## This project The product will continue to evolve.
### I ask and encourage you to use the product, and ask for comments and recommendations for improvement.

#### Thanks in advance
# Yizhak Orfanian
