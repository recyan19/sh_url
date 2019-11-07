README for sh_url (guide for Ubuntu):

1) You need to have installed python3, virtualenv, pip, git, httpie(install via pip) or curl on your local machine.
2) Clone project: git clone https://github.com/recyan19/sh_url.git
3) Change directory: cd PROJECT_DIR;
4) Create and activate virtual environment: python3 -m venv env; source env/bin/activate
5) Install all requirements: pip install requirements.txt
6) For testing: python manage.py test
7) Create all database migrations: python manage.py makemigrations; python manage.py migrate
7) Create an admin user: python manage.py createsuperuser
8) For launching local server: python manage.py runserver


API:

endpoints:
1) /api/users/
2) /api/users/<int:pk>/
3) /api/urls/
4) /api/urls/<str:url_id>/

To create an url as authenticated user:
1) http -a username:password --form POST url="url" days="days"
unauthenticated:
2) http -a --form POST "url"
To get info about shortened url: 
3)http -a username:password http://localhost:8000/api/urls/<str:url_id>/
