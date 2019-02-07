def app_list(app_name, dst):

	content = "\
{% extends '"+app_name+"/base.html' %}\n\
{% block content %}\n\
<h1>"+app_name+" List</h1>\n\
<hr>\n\
<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_create' %}\">Create</a>\n\
<hr>\n\
{% if "+app_name[0:-1]+"_list %}\n\
	{% for "+app_name[0:-1]+" in "+app_name[0:-1]+"_list %}\n\
		<a href=\"{% url '"+app_name+":"+app_name[0:-1]+"_detail' slug="+app_name[0:-1]+".slug %}\"><p>{{"+app_name[0:-1]+".user}}</p></a>\n\
		<p>{{"+app_name[0:-1]+".slug}}</p>\n\
		<p>{{"+app_name[0:-1]+".name}}</p>\n\
		<p>{{"+app_name[0:-1]+".address}}</p>\n\
		<p>{{"+app_name[0:-1]+".description}}</p>\n\
	{% endfor %}\n\
{% else %}\n\
<p>No Locations</p>\n\
{% endif %}\n\
{% endblock %}"

	f = open(dst, 'w')
	f.write(content)
	f.close()

