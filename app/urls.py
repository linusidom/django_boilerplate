def urls_template(app_name, dst):
	
	content = "\
from django.urls import path, re_path\n\
from "+app_name+" import views\n\
from "+app_name+".models import "+app_name[0:-1].title()+"\n\n\
app_name='"+app_name+"'\n\n\
urlpatterns=[\n\
	path('',views.IndexTemplateView.as_view(), name = 'index'),\n\
	path('list/',views."+app_name[0:-1].title()+"ListView.as_view(), name = '"+app_name[0:-1]+"_list'),\n"
	
	if app_name == 'accounts':
		content += "\
	path('signup/',views.signup, name = 'signup'),\n\
	re_path('detail/(?P<pk>\d+)/',views."+app_name[0:-1].title()+"DetailView.as_view(), name = '"+app_name[0:-1]+"_detail'),\n\
	re_path('update/(?P<pk>\d+)/',views.update_account, name = '"+app_name[0:-1]+"_update'),\n\
	re_path('delete/(?P<pk>\d+)/',views."+app_name[0:-1].title()+"DeleteView.as_view(), name = '"+app_name[0:-1]+"_delete'),\n]"

	else:
		content += "\
	path('create/',views."+app_name[0:-1].title()+"CreateView.as_view(), name = '"+app_name[0:-1]+"_create'),\n\
	re_path('detail/(?P<slug>[-\w]+)/',views."+app_name[0:-1].title()+"DetailView.as_view(), name = '"+app_name[0:-1]+"_detail'),\n\
	re_path('update/(?P<slug>[-\w]+)/',views."+app_name[0:-1].title()+"UpdateView.as_view(), name = '"+app_name[0:-1]+"_update'),\n\
	re_path('delete/(?P<slug>[-\w]+)/',views."+app_name[0:-1].title()+"DeleteView.as_view(), name = '"+app_name[0:-1]+"_delete'),\n]"

	f = open(dst, 'w')
	f.write(content)
	f.close()