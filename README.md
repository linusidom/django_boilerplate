# django_create_base

This fill structure helps create the inital files needed to start a custom Accounts App, any supporting apps with forms, models, views and urls arlready preset and updates the settings files with the necessary components.

Required Packages:
```
# Added by script to project settings.py
pip install livereload
pip install djangorestframework

#optional for funtional testing
pip install selenium
```

Ex Usage
Copy the folder structure to a folder outside of the main project structure

```
~ Admin$ git clone https://github.com/linusidom/django_create_base.git
```

From within the project root, run the create_base.py file.

## Create base django project
```
~ Admin$ django-admin startproject test_project
~ Admin$ cd test_project
test_project Admin$ 
```

## Create apps within django proect
```
test_project Admin$ django-admin startapp accounts
test_project Admin$ django-admin startapp test1_apps
test_project Admin$ django-admin startapp test2_apps
```

# Run create_base.py from within the project_root
```
~ Admin$ ../django_create_base/create_base.py accounts test_app1 test_app2
```

## Project Files ~/project_root/project_root
Settings.py updated with all the necessary apps, templates, static_url, static_root, media_url, media_root, login/logout_redirect_url and login_url
Urls.py updated with all the new apps, login/logout, and self-service password management
Views.py populated with basic redirect to index.html

## Project Templates
Base.html is setup with basic links to all apps and if Account is present, Login, Logout and Link to Account Detail
registration folders is created with all files necessary for self-service password maintenance

## Accounts is setup as follows (if present)
accounts/templates/accounts -> all template files based on model name "Account"
accounts/models.py, views.py, urls.py, forms.py
- Account Model is based on AbstractUser
- Custom Signup View and login with E-mail

## All other apps are setup based on the following
test1_apps/templates/test1_apps -> all template files based on model name "Test1_app"
test1_apps/models.py, views.py, urls.py, forms.py, utils.py
- Test1_app Model is based on models.Model
- Test1_app models.py comes with name and slug fields with randomizing script for slug field from utils.py






