# API_SoftDesk# API_SoftDesk
Project done for my OpenClassrooms Python Application Developer course.  
This is an API made with Django for a fictitious company, SoftDesk.  
The application is used to report projects issues. 

## Features

All endpoints, their details and examples of use are described in the 
[documentation](https://documenter.getpostman.com/view/23455413/2s8Z73xAP1). 

## Installation

Launch the console, go to the folder of your choice and clone this repository:
```
git clone https://github.com/Bimarsto/API_SoftDesk.git
```
Go to the API_SoftDesk folder and create a new virtual environment:
```
python -m venv env
```
Then activate it.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Then install the required packages:
```
pip install -r requirements.txt
```
Then, go to the root of the project (where the manage.py file is located), and make the migrations:
```
python manage.py makemigrations
```
then apply the migrations: 
```
python manage.py migrate
```
You can now run the serveur: 
```
python manage.py runserver
```
You can then use the application via the different endpoints described in the documentation. 
You must first create a user account at the endpoint http://127.0.0.1:800/api/signup/ in order to access the application's functionality.
