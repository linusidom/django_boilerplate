def views_project(dst):
	
	content = "from django.shortcuts import render\n\
\n\
# Create your views here.\n\
from django.views.generic import TemplateView\n\
\n\
class IndexTemplateView(TemplateView):\n\
	template_name='index.html'"

	f = open(dst, 'w')
	f.write(content)
	f.close()