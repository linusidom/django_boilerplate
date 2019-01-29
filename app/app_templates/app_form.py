def app_form(app_name, dst):

	content = "\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<h1>"+app_name+" Create/Update</h1>\n\
\n\
	<form method='POST'>\n\
		{%csrf_token%}\n\
		{{form.as_p}}\n\
		<input type='submit' value='Save'>\n\
	</form>\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()