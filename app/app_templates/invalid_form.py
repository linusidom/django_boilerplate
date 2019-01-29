def invalid_form(app_name, dst):
	
	content = "\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<p>e-mail already in use</p>\n\
<a href=\"{% url '"+app_name+":signup'%}\">Signup</a>\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()
