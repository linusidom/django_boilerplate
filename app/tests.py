def tests_template(app_name, dst):

	model_name = app_name[:-1].title()

	content = f"""from django.test import TestCase
from {app_name}.models import {model_name}
	
class {app_name.title()}HomePage(TestCase):
	def test_{app_name}_home_page(self):
		request = self.client.get('/{app_name}/')
		self.assertEqual(request.status_code, 200)
	def test_{app_name}_list(self):
		request = self.client.get('/{app_name}/list/')
		self.assertEqual(request.status_code, 200)
	def test_{app_name}_create(self):
		request = self.client.get('/{app_name}/create/')
		self.assertEqual(request.status_code, 200)
	def test_{app_name}_detail(self):
		name = 'Test Name'
		{app_name} = {model_name}.objects.create(name=name)
		request = self.client.get('/{app_name}/detail/test-name/')
		self.assertEqual(request.status_code, 200)
	def test_{app_name}_update(self):
		name = 'Test Name'
		{app_name} = {model_name}.objects.create(name=name)
		request = self.client.get('/{app_name}/update/test-name/')
		self.assertEqual(request.status_code, 200)
	def test_{app_name}_delete(self):
		name = 'Test Name'
		{app_name} = {model_name}.objects.create(name=name)
		request = self.client.get('/{app_name}/delete/test-name/')
		self.assertEqual(request.status_code, 200)
	"""

	f = open(dst, 'w')
	f.write(content)
	f.close()