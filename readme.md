Backend of Truecaller kinda app!

### Prerequisite
Python 3.11.0 


### Project Specifications
Framework - Django 5.0.6 <br/>
Database - sqlite


### How to run project?
1. Download project
2. Create .env file, if not present, in directory - (BASE_DIRECTORY/instacaller) and add env variables in it from .env_example. Set env variables accordingly while releasing to production.
3. (Recommended but not mandatory) Create virtual invironment
> pipenv shell # or via any other method
4. Install dependencies (make sure you are in currect directory which is base directory)
> pip install -r requirements.txt
5. (Optional) - Create super user for django admin
> python manage.py createsuperuser
6. Run migrations 
> python manage.py migrate
7. Run server
> python manage.py runserver

