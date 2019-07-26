def admin_template(app_name, dst):
	
	app_model = app_name[:-1].title()
	content = f"""from django.contrib import admin

# Register your models here.

from {app_name}.models import {app_model}

admin.site.register({app_model})"""

	f = open(dst, 'w')
	f.write(content)
	f.close()