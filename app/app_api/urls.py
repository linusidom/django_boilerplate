from django.urls import path, re_path
from '+app_name+'.api import views

app_name = 'api_+app_name+'

urlpatterns = [
	path('(?P<pk>\d+)',views.'+app_name.title()+'RUDAPIView.as_view(),name='api_'+app_name+),
]