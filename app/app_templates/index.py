def index(app_name, dst):

	content = "\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<h1>"+app_name+" HTML</h1>\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()