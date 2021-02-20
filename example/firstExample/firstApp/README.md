# register admin user
`cd firstApp`<br>
`create admin.py`<br>
`python3 manage.py makemigrates`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
 cav_edu/cav_edu<br>
Register user to admin site in admin.py file<br>
Login to `http://localhost:8000/admin/`

# create migrations and install DB browser for SQLite
create models in models.py<br>
` python3 manage.py makemigrations firstApp`<br>
` python3 manage.py migrate`<br>
`sudo apt-get install sqlitebrowser`<br>

#  Run app
`python3 manage.py runserver`<br>

