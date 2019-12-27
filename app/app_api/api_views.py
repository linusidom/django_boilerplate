def api_views(app_name, dst):

	app_model = app_name[:-1].title()

	content = f"""from rest_framework import generics
from {app_name}.api.models import {app_model}Serializer
from {app_name}.models import {app_model}

class {app_model}ListAPIView(generics.ListAPIView):
	serializer_class = {app_model}Serializer
	queryset = {app_model}.objects.all()"""

	f = open(dst, 'w')
	f.write(content)
	f.close()