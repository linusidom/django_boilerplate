def forms_template(app_name, dst):
	
	app_model = app_name[:-1].title()

	if app_name == 'accounts':
		content = f"""\
from django import forms
from django.contrib.auth.forms import UserCreationForm
from {app_name}.models import {app_model}

class {app_model}Form(UserCreationForm):
	class Meta():
		model = {app_model}
		fields = ['email','password1','password2']

class {app_model}UpdateForm(forms.ModelForm):
	class Meta():
		model = {app_model}
		fields = ['email']"""

	else:
		content = f"""\
from django import forms
from {app_name}.models import {app_model}
class {app_model}Form(forms.ModelForm):
	class Meta():
		model = {app_model}
		exclude = ['slug']"""

	

	f = open(dst, 'w')
	f.write(content)
	f.close()



