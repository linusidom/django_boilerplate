def base_project(app_name, dst):

	content = "\
<!DOCTYPE html>\n\
{% load static %}\n\
<html>\n\
<head>\n\
	<title>BASE</title>\n\
	<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n\
	<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n\
	<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n\
    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n\
	<link rel=\"stylesheet\" type=\"text/css\" href=\"{% static 'css/mysite.css' %}\">\n\
</head>\n\
<body>\n\
<header>\n\
	<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">\n\
  	<a class=\"navbar-brand\" href=\"#\">Navbar</a>\n\
  	<button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarNavAltMarkup\" aria-controls=\"navbarNavAltMarkup\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n\
    	<span class=\"navbar-toggler-icon\"></span>\n\
  	</button>\n\
  	<div class=\"collapse navbar-collapse\" id=\"navbarNavAltMarkup\">\n\
    	<div class=\"navbar-nav\">\n\
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
	</div>\n\
	</nav>\n\
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