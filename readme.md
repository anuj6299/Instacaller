###Project Details
I build this as an assignment for [Instahyre](https://www.instahyre.com/) as their round 1 of interview process. The assignement was to build backend for truecaller kinda app. You can find more details in the pdf (coding_task.pdf) present in this repo.

### Prerequisite
Python 3.11.0 


### Project Specifications
Framework - Django 5.0.6
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
6. Run server
> python manage.py runserver


### Assumptions for this project
1. It is not mentioned in the doc if "search contact by name" API and "search contact by phone" API should be same or different api so I have kept separate apis for both use cases.
2. User and contacts scale is not very high (less than 1lakh rows). If scale is high, we can easily increase performance by adding database indexing (have addded comment also in the code) and even cache (redis) if needed. There are more possible optimizations depending on scale, need and budget.

