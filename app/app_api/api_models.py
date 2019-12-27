def api_models(app_name, dst):

	app_model = app_name[:-1].title()

	content = f"""from rest_framework import serializers
from {app_name}.models import {app_model}

class {app_model}Serializer(serializers.ModelSerializer):
	class Meta():
		model = {app_model}
		fields = ['id','name','slug']"""

	f = open(dst, 'w')
	f.write(content)
	f.close()