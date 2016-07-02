Demo
===============
host : http://awo174.app.activewizards.com
user : admin@admin.com
pwd : 12344321a

Setup
===============
- install Python3, Mysql, nodejs, npm
- pip install -r requirements.txt
- bower install
- change db settings in config/local_settings.py
- ./manage.py migrate --database={your-users-db-name}
- ./manage.py migrate --database={your-logs-db-name}
- ./manage.py createsuperuser (create admin user)
- ./manage.py runserver
