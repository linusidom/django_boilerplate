import os
import shutil
import re

def urls_project(app_name, dst = '/', proj_name='test_bidding'):
    
	arr = []
	urlpatterns = 0
	urlpatterns_paren = 0
	src_proj_files = '/Users/Admin/coding/django/django_create_base/proj_files'

	# Copy the settings file from the project directory to another settings file in the same project directory

	pattern = r'^]$'

	shutil.copy(proj_name+'/urls.py', proj_name+'/urls_orig.py')

	f = open(proj_name + '/urls_orig.py','r')
	contents = f.readlines()
	f.close()

	if '#updated' not in contents[-1]:
		test_arr = ['']*2
		header = f"""from {proj_name} import views, settings
from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = ["""

		urlpatterns = f"""
	path('admin/', admin.site.urls),
	path('', views.IndexTemplateView.as_view(), name='index'),
	
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'user_login'),
	path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),
	
	path('change-password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_logout')), name='password_change'),
	path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),"""

		test_arr[0] = header

		test_arr[1] = urlpatterns

		for app in app_name:
			app_urlpattern = f"""
	path('{app}/',include('{app}.urls', namespace = '{app}')),
	path('api/{app}/',include('{app}.api.urls',namespace='api_{app}')),"""
			test_arr.append(app_urlpattern)

		# test_arr[1] += arr
		test_arr.append(f"""
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#updated DO NOT REMOVE THIS LINE""")

		f = open(proj_name + '/urls.py', 'w')
		for line in test_arr:
		# print(line)
			f.write(line)
		f.close()

	else:
		existing_apps = []
		for i in range(len(contents)):
			if "urlpatterns = [" in contents[i]:
				urlpatterns_paren = 1
				start_urlpatterns_index = i + 1
			elif re.match(pattern, contents[i]) and urlpatterns_paren:
				urlpatterns_paren = 0
				end_urlpatterns_index = i
		for i in range(start_urlpatterns_index, end_urlpatterns_index):
			contents[i] = contents[i].strip()
			# print('orig',contents[i])
			if contents[i] != '':
				url_app_names = contents[i].split('\'')[1]
				existing_apps.append(url_app_names[0:-1])
			arr.append(contents[i])
		
		for app in app_name:
			if app not in existing_apps:
				arr.append(f"""
	path('{app}/',include('{app}.urls', namespace = '{app}')),
	path('api/{app}/',include('{app}.api.urls',namespace = 'api_{app}')),""")
		# for item in arr:
		# 	print(item)
		del contents[start_urlpatterns_index - 1:]

		# print(contents)

		j = 0
		contents.insert(start_urlpatterns_index - 1, "urlpatterns = [\n")
		# for i in range(start_urlpatterns_index, end_urlpatterns_index + len(app_name)):
		for j in range(len(arr)-1, -1, -1):
			if arr[j] != '':
				contents.insert(start_urlpatterns_index,"    "+arr[j]+"\n")
			if j == 0:
				contents.insert(start_urlpatterns_index + len(arr), f"""
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#updated DO NOT REMOVE THIS LINE""")
		
		f = open(proj_name + '/urls.py', 'w')
		for line in contents:
		# print(line)
			f.write(line)
		f.close()
