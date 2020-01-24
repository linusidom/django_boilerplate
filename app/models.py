def models_template(models_need_user, app_name, dst, proj_name):

	app_model = app_name[:-1].title()
	app_name_short = app_name[:-1]

	image_upload_config = f"""
def update_image_name(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,986987)
	name, ext = update_image_name(filename)
	final_filename = f'{{new_filename}}{{ext}}'
	return f'{app_name}/{{new_filename}}/{{final_filename}}'

	"""

	content = f"""
import random, os
from django.db import models
from django.shortcuts import reverse
from {app_name}.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from {proj_name} import settings"""
	
	if app_name == 'accounts':
		content += f"""
from django.contrib.auth.models import AbstractUser

{image_upload_config}

class Account(AbstractUser):"""
	elif models_need_user:
		content += f"""


User = settings.AUTH_USER_MODEL

{image_upload_config}

class {app_model}(models.Model):"""
	
	else:
		content += f"""

{image_upload_config}

class {app_model}(models.Model):"""

	if models_need_user and app_name != 'accounts':
		content += f"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)"""

	content += f"""
	name = models.CharField(max_length=100, null=True, blank=True)
	slug = models.SlugField(unique=True, blank=True)"""

	
	if app_name == 'accounts':
		content += f"""
	
	def __str__(self):
		return self.email"""
	else:
		content += f"""
	
	def __str__(self):
		return self.name"""

	content += f"""
	
	@property
	def title(self):
		return self.name

	def get_absolute_url(self):
		return reverse('{app_name}:{app_name_short}_detail', kwargs={{'slug':self.slug}})"""
	if app_name != 'accounts':
		content += f"""
		
def pre_slug_field(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_slug_field, sender={app_model})"""
	
	f = open(dst, 'w')
	f.write(content)
	f.close()