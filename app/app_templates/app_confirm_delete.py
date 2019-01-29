def app_confirm_delete(app_name, dst):

	content="\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<h1>"+app_name+" Delete</h1>\n\
\n\
	<form method=\'POST\'>\n\
		{%csrf_token%}\n\
		Are you sure you want to Delete {{object}}?\n\
		<input type=\'submit\' value=\'Delete\'>\n\
	</form>\n\
{% endblock %}"
	
	f = open(dst, 'w')
	f.write(content)
	f.close()