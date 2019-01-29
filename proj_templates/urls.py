def urls_project(app_name, dst, proj_name):

	content = "\
from django.contrib import admin\n\
from django.urls import path, include, re_path, reverse_lazy\n\
from "+proj_name+" import views, settings\n\
from django.contrib.auth import views as auth_views\n\
from django.conf.urls.static import static\n\
\n\
\n\
urlpatterns = [\n\
	path('admin/', admin.site.urls),\n\
	path('', views.IndexTemplateView.as_view(), name='index'),\n\n"

	for app in app_name:
		content += "\
	path('"+app+"/', include('"+app+".urls', namespace='"+app+"')),\n"

	content += "\n\
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'user_login'),\n\
	path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),\n\
	\n\
	path('change-password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_logout')), name='password_change'),\n\
	path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),\n\
	\n\
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),\n\
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),\n\
	re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',\n\
	auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),\n\
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),\n\
]\n\
\n\
\n\
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\n\
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"

	f = open(dst, 'w')
	f.write(content)
	f.close()