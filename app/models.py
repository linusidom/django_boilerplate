def models_template(app_name, dst, proj_name):

	content = "\
from django.db import models\n\
from django.shortcuts import reverse\n\
from "+app_name+".utils import unique_slug_generator\n\
from django.db.models.signals import pre_save\n\
from "+proj_name+" import settings\n"
	
	if app_name == 'accounts':
		content += "\
from django.contrib.auth.models import AbstractUser\n\n\
class Account(AbstractUser):\n"
	else:
		content += "\n\
class "+app_name[0:-1].title()+"(models.Model):\n"

	content += "\
	name = models.CharField(max_length=100, null=True, blank=True)\n"

	if app_name != 'accounts':
		content += "\
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)\n\
	slug = models.SlugField(unique=True, blank=True)\n\
	\n"

	if app_name == 'accounts':
		content += "\
	def __str__(self):\n\
		return self.email\n\
	\n"
	else:
		content += "\
	def __str__(self):\n\
		return self.name\n\
	\n"

	content += "\
	@property\n\
	def title(self):\n\
		return self.name\n\
	\n\
	def get_absolute_url(self):\n\
		return reverse('"+app_name+":"+app_name[0:-1]+"_detail', kwargs={'slug':self.slug})\
\n"
	if app_name != 'accounts':
		content += "\
def pre_slug_field(sender, instance, *args, **kwargs):\n\
	if not instance.slug:\n\
		instance.slug = unique_slug_generator(instance)\n\
\n\
pre_save.connect(pre_slug_field, sender="+app_name[0:-1].title()+")"
	
	f = open(dst, 'w')
	f.write(content)
	f.close()