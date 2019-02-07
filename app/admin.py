def admin_template(app_name, dst):
	content = "from django.contrib import admin\n\
\n\
# Register your models here.\n\
\n\
from "+app_name+".models import "+app_name[0:-1].title()+"\n\
\n\
admin.site.register("+app_name[0:-1].title()+")"

	f = open(dst, 'w')
	f.write(content)
	f.close()