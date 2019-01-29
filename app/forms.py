def forms_template(app_name, dst):
	

	if app_name == 'accounts':
		content = "\
from django import forms\n\
from django.contrib.auth.forms import UserCreationForm\n\
from "+app_name+".models import "+app_name[0:-1].title()+"\n\n\
\n\
class "+app_name[0:-1].title()+"Form(UserCreationForm):\n\
	class Meta():\n\
		model = "+app_name[0:-1].title()+"\n\
		fields = ['email','password1','password2']\n\
\n\n\
class "+app_name[0:-1].title()+"UpdateForm(forms.ModelForm):\n\
	class Meta():\n\
		model = "+app_name[0:-1].title()+"\n\
		fields = ['email']"

	else:
		content = "\
from django import forms\n\
from "+app_name+".models import "+app_name[0:-1].title()+"\n\n\
class "+app_name[0:-1].title()+"Form(forms.ModelForm):\n\
	class Meta():\n\
		model = "+app_name[0:-1].title()+"\n\
		fields = []"

	

	f = open(dst, 'w')
	f.write(content)
	f.close()



