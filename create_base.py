import os

from os import path
import sys
import shutil
# app_name = 'groups'
import proj_templates.urls as urls_project
import proj_templates.views as views_project
import proj_templates.settings as settings_project
import proj_templates.proj_base as base_project


from app import forms, urls, views, models, admin
from app.app_api import api_models, api_views, api_urls 
from app.app_templates import (app_confirm_delete,
							app_detail, app_form,
							app_list, base, index,
							signup, invalid_form)



src_templates = '/Users/Admin/coding/django/django_create_base/templates/'
src_static = '/Users/Admin/coding/django/django_create_base/static/'
src_functional_tests = '/Users/Admin/coding/django/django_create_base/functional_tests/'
src_utils_file = '/Users/Admin/coding/django/django_create_base/app/utils.py'


# Project Files (URLS, Views, Settings, Base)
proj_name = os.getcwd().split('/')[-1]
proj_root = os.getcwd()
proj_dst = os.getcwd()+'/'+proj_name

print(proj_root+'/manage.py')

if not os.path.exists(proj_root+'/manage.py'):
	print("You're in the wrong folder...", proj_root)
	exit(1)

print('building', proj_name, end='')
app_names = sys.argv[1:]

urls_project.urls_project(app_name=app_names, dst=proj_dst+'/urls.py', proj_name=proj_name)
views_project.views_project(dst=proj_dst+'/views.py')
settings_project.settings_project(app_name=app_names, dst=proj_dst+'/settings.py', proj_name = proj_name)
base_project.base_project(app_name=app_names, dst=src_templates+'/base.html')



# App Folders

proj_folders_SRC = [src_templates, src_static, src_functional_tests]
proj_folders_DST = ['./templates', './static', './functional_tests']

for i in range(len(proj_folders_DST)):
	if not os.path.exists(proj_folders_DST[i]):
		shutil.copytree(proj_folders_SRC[i], proj_folders_DST[i])
print('...finished')


# Proejct App Folders and Files (URLS, Views, Settings, Base, etc.)
for app_name in app_names:
	# if app_name != sys.argv[0]:
	# app_templates = app_name+'/templates/'+app_name
	print('building', app_name, end='')
	
	# App Folder
	if not os.path.exists(app_name):
		os.mkdir(app_name)
	
	# App files...forms, urls, utils, views, models, admin
	if not os.path.exists(app_name+'/forms.py'):
		forms.forms_template(app_name=app_name, dst=app_name+'/forms.py')
	
	if not os.path.exists(app_name+'/urls.py'):
		urls.urls_template(app_name=app_name, dst=app_name+'/urls.py')

	if not os.path.exists(app_name+'/utils.py'):
		shutil.copy(src_utils_file, proj_root+'/'+app_name+'/utils.py')

	views.views_template(app_name=app_name, dst=app_name+'/views.py')
	models.models_template(app_name=app_name, dst=app_name+'/models.py', proj_name=proj_name)
	admin.admin_template(app_name=app_name, dst=app_name+'/admin.py')
		
	# App templates app_name/templates/app_name/...
	if not os.path.exists(app_name+'/templates'):
		os.mkdir(app_name+'/templates/')
		os.mkdir(app_name+'/templates/'+app_name)

		dst_app_name = app_name+'/templates/'+app_name+'/'+app_name[0:-1]

		app_confirm_delete.app_confirm_delete(app_name=app_name, dst=dst_app_name+'_confirm_delete.html')
		app_detail.app_detail(app_name=app_name, dst=dst_app_name+'_detail.html')
		app_form.app_form(app_name=app_name, dst=dst_app_name+'_form.html')
		app_list.app_list(app_name=app_name, dst=dst_app_name+'_list.html')
		base.base(app_name=app_name, dst=app_name+'/templates/'+app_name+'/base.html')
		index.index(app_name=app_name, dst=app_name+'/templates/'+app_name+'/index.html')
		
		if app_name == 'accounts':
			signup.signup(app_name=app_name, dst=app_name+'/templates/'+app_name+'/signup.html')
			invalid_form.invalid_form(app_name=app_name, dst=app_name+'/templates/'+app_name+'/invalid_form.html')

	# API Folders and Files
	if not os.path.exists(app_name+'/api'):
		os.mkdir(app_name+'/api/')
		api_models.api_models(app_name=app_name, dst=app_name+'/api/models.py')
		api_urls.api_urls(app_name=app_name, dst=app_name+'/api/urls.py')
		api_views.api_views(app_name=app_name, dst=app_name+'/api/views.py')
		

	print('...finished')
















