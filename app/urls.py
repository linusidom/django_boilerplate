def urls_template(app_name, dst):
	
	app_model = app_name[:-1].title()
	app_name_short = app_name[:-1]
	content = f"""from django.urls import path, re_path
from {app_name} import views


app_name='{app_name}'

urlpatterns=[
	path('',views.IndexTemplateView.as_view(), name = 'index'),
	path('list/',views.{app_model}ListView.as_view(), name = '{app_name_short}_list'),"""
	
	if app_name == 'accounts':
		content += f"""
	path('signup/',views.signup, name = 'signup'),
	re_path(r'^detail/(?P<pk>\d+)/',views.{app_model}DetailView.as_view(), name = '{app_name_short}_detail'),
	re_path(r'^update/(?P<pk>\d+)/',views.update_account, name = '{app_name_short}_update'),
	re_path(r'^delete/(?P<pk>\d+)/',views.{app_model}DeleteView.as_view(), name = '{app_name_short}_delete'),

]"""

	else:
		content += f"""
	path('create/',views.{app_model}CreateView.as_view(), name = '{app_name_short}_create'),
	re_path(r'^detail/(?P<slug>[-\w]+)/',views.{app_model}DetailView.as_view(), name = '{app_name_short}_detail'),
	re_path(r'^update/(?P<slug>[-\w]+)/',views.{app_model}UpdateView.as_view(), name = '{app_name_short}_update'),
	re_path(r'^delete/(?P<slug>[-\w]+)/',views.{app_model}DeleteView.as_view(), name = '{app_name_short}_delete'),

]"""

	f = open(dst, 'w')
	f.write(content)
	f.close()