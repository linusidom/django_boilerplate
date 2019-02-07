def app_detail(app_name, dst):

	content = "\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<h1>"+app_name+" Detail</h1>\n\
\n"
	

	if app_name == 'accounts':
		content += "\n\
<p>{{"+app_name[0:-1]+".username}}</p>\n\
<p>{{"+app_name[0:-1]+".email}}</p>\n"

	else:
		content += "\
<hr>\n\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_create' %}\">Create</a>\n\
<hr>\n\
<p>{{"+app_name[0:-1]+".name}}</p>\n\
<p>{{"+app_name[0:-1]+".slug}}</p>\n"

	if app_name == 'accounts':
		content += "\
<a href=\"{% url 'password_change' %}\">Change Password</a>\n\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_update' pk=account.pk %}\">Update</a>\n\
\n\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_delete' pk=account.pk %}\">Delete</a>\n\
\n\
{% endblock %}"

	else:
		content += "\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_update' slug="+app_name[0:-1]+".slug %}\">Update</a>\n\
\n\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_delete' slug="+app_name[0:-1]+".slug %}\">Delete</a>\n\
\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()