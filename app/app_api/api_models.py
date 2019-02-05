def api_models(app_name, dst):

	content = "from rest_framework import serializers\n\
from '"+app_name+"'.models import '"+app_name.title()+"'\n\
\n\
class '"+app_name.title()+"'Serializer(serializers.ModelSerializer):\n\
	class Meta():\n\
		model = "+app_name.title()+""

	f = open(dst, 'w')
	f.write(content)
	f.close()