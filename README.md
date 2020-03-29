# django_boilerplate

This file structure helps create the inital files needed to start a custom Accounts App, any supporting apps with forms, models, views and urls arlready preset and updates the settings files with the necessary components.

Required Packages:
```
# Added by script to project settings.py
pip install django-livereload-server
pip install djangorestframework
```

Optional Packages
```
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
test_project Admin$ django-admin startapp example1_apps
test_project Admin$ django-admin startapp example2_apps
```

# Run create_base.py from within the project_root
```
test_project Admin$ ../django_create_base/create_base.py accounts example1_apps example2_apps
```

## Project Files ~/project_root/project_root/settings.py
- updates INSTALLED_APPS, TEMPLATE_DIR, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, LOGIN_URL as well as AUTH_USER_MODEL if accounts are added
- urls.py updated with all apps pointing to ```apps/urls.py```, Django auth_view.LoginView and LogoutView, as well as self-service password management
- views.py populated with basic redirect to ```templates/index.html```


## Project Templates
Base.html is setup with basic links to all apps and if Account is present, Login, Logout and Link to Account Detail
registration folders is created with all files necessary for self-service password maintenance

## (Optional) Accounts is setup as follows
accounts/templates/accounts -> all template files based on model name "Account"
accounts/models.py, views.py, urls.py, forms.py
- Account Model is based on AbstractUser
- Custom Signup View and login with E-mail

## All other apps are setup based on the following
example1_apps/templates/test1_apps -> all template files based on model name "Example1_app"
- Creates example1_apps/models.py, views.py, urls.py, forms.py, utils.py
- example1_apps Model is based on models.Model
- example1_apps models.py comes with name and slug fields with randomizing script for slug field from utils.py






