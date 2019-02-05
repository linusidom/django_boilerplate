def api_views(app_name, dst):

	content = "from rest_framework import generics\n\
from '"+app_name+"'.api.models import '"+app_name.title()+"'Serializer\n\
from '"+app_name+"'.models import '"+app_name.title()+"'\n\
\n\
class '"+app_name.title()+"RUDAPIView(generics.RetrieveUpdateDestroyAPIView):\n\
	lookup ='pk'\n\
	serializer_class = '"+app_name.title()+"'Serializer\n\
	queryset = '"+app_name.title()+"'.objects.all()'"

	f = open(dst, 'w')
	f.write(content)
	f.close()