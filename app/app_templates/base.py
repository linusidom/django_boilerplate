def base(app_name, dst):

	content = "\
{% extends 'base.html' %}\n\
{% block content %}\n\
<h1>App Base HTML</h1>\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()