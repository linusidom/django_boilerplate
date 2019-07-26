def api_urls(app_name, dst):

	app_model = app_name[:-1].title()
	app_name_short = app_name[:-1]

	content = f"""from django.urls import path, re_path
from {app_name}.api import views

app_name = 'api_{app_name}'

urlpatterns = [
	path('list/',views.{app_model}ListAPIView.as_view(),name='api_{app_name_short}_list'),
]"""

	f = open(dst, 'w')
	f.write(content)
	f.close()