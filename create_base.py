import os

from os import path
import sys
import shutil
# app_name = 'groups'
import proj_templates.urls as urls_project
import proj_templates.views as views_project
import proj_templates.settings as settings_project
import proj_templates.proj_base as base_project


from app import forms, urls, views, models
from app.app_templates import (app_confirm_delete,
							app_detail, app_form,
							app_list, base, index,
							signup, invalid_form)


src_templates = '/Users/Admin/coding/django/django_create_base/templates/'
src_static = '/Users/Admin/coding/django/django_create_base/static/'
utils_file = '/Users/Admin/coding/django/django_create_base/app/utils.py'


app_names = sys.argv[1:]

proj_name = os.getcwd().split('/')[-1]
proj_root = os.getcwd()
proj_dst = os.getcwd()+'/'+proj_name

with open(proj_dst+'/settings.py') as f:
	for line in f:
		if 'SECRET_KEY' in line:
			secret_key = line

# Project Files (URLS, Views, Settings, Base)

urls_project.urls_project(app_name=app_names, dst=proj_dst+'/urls.py', proj_name=proj_name)
views_project.views_project(dst=proj_dst+'/views.py')
settings_project.settings_project(app_name=app_names, dst=proj_dst+'/settings.py', secret_key=secret_key, project_name = proj_name)
base_project.base_project(app_name=app_names, dst=src_templates+'/base.html')


for app_name in sys.argv:
	if app_name != sys.argv[0]:
		app_templates = app_name+'/templates/'+app_name
		print('building', app_name, end='')
		
		# Project Folders
		if not os.path.exists('./templates'):
			shutil.copytree(src_templates, './templates')
		
		if not os.path.exists('./static'):
			shutil.copytree(src_static, './static')
		

		# App Folder
		if not os.path.exists(app_name):
			os.mkdir(app_name)
		

		# App files
		if not os.path.exists(app_name+'/forms.py'):
			forms.forms_template(app_name=app_name, dst=app_name+'/forms.py')
		
		if not os.path.exists(app_name+'/urls.py'):
			urls.urls_template(app_name=app_name, dst=app_name+'/urls.py')

		if not os.path.exists(app_name+'/utils.py'):
			shutil.copy(utils_file, proj_root+'/'+app_name+'/utils.py')
		# if not os.path.exists(app_name+'/views.py'):
		views.views_template(app_name=app_name, dst=app_name+'/views.py')
		models.models_template(app_name=app_name, dst=app_name+'/models.py')
		
		# App templates
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

		print('...finished')