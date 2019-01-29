def base_project(app_name, dst):

	content = "\
<!DOCTYPE html>\n\
{% load staticfiles %}\n\
<html>\n\
<head>\n\
	<title>BASE</title>\n\
	<link rel=\"stylesheet\" type=\"text/css\" href=\"{% static 'css/mysite.css' %}\">\n\
</head>\n\
<body>\n\
<header>\n\
	<ul>\n\
		<li><a href=\"{% url 'index' %}\">Index</a></li>\n"

	for app in app_name:
		content += "\
		<li><a href=\"{% url '"+app+":"+app[0:-1]+"_list' %}\">"+app[0:-1].title()+"</a></li>\n"


	for app in app_name:
		if app == 'accounts':
			content += "\
		<li><a href=\"{% url '"+app+":signup' %}\">Signup</a></li>\n\
		<li><a href=\"{% url 'user_login' %}\">Login</a></li>\n\
		{% if user.is_authenticated %}\n\
			<li><a href=\"{% url 'user_logout' %}\">Logout</a></li>\n\
			<li><a href=\"{% url '"+app+":"+app[0:-1]+"_detail' pk=user.pk %}\">"+app[0:-1].title()+" Detail</a></li>\n\
		{% endif %}\n"

	content += "\
	</ul>\n\
</header>\n\
<div class=\"container\">\n\
{% block content %}\n\
{% endblock %}\n\
</div>\n\
</body>\n\
</html>"

	f = open(dst, 'w')
	f.write(content)
	f.close()