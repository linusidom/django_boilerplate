def api_urls(app_name, dst):

	content = "from django.urls import path, re_path\n\
from '"+app_name+"'.api import views\n\
\n\
app_name = 'api_"+app_name+"'\n\
\n\
urlpatterns = [\n\
	path('(?P<pk>\d+)',views.'"+app_name.title()+"'RUDAPIView.as_view(),name='api_'"+app_name+"),\n\
]"

	f = open(dst, 'w')
	f.write(content)
	f.close()