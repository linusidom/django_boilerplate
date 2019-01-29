import os
import shutil

def settings_project(app_names=['accounts','campaigns','locations']):

    content = ""

    src_proj_files = '/Users/Admin/coding/django/django_create_base/proj_files'

    # Copy the settings file from the project directory to another settings file in the same project directory
    
    proj_root = os.getcwd()
    proj_name = os.getcwd().split('/')[-1]
    print('test', proj_root, proj_name)
    shutil.copy(proj_name+'/settings.py', proj_name+'/settings_orig.py')

    # update the settings file with the 
    # templates Dirs
    f = open(proj_name+'/settings_new.py','w')
    with open(proj_name+'/settings_orig.py') as s:
        lines = s.readlines()
        for i in range(len(lines)):
            lines[i].strip()
            if lines[i].startswith('BASE_DIR') and not lines[i+1].startswith('TEMPLATE_DIR'):
                
                lines[i] += "TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')\n\
STATIC_DIR = os.path.join(BASE_DIR, 'static')\n"
            if "'DIRS': []," in lines[i]:
                lines[i] = "        'DIRS': [TEMPLATE_DIR,],\n"
            if "'django.contrib.staticfiles'," in lines[i] and 'livereload' not in lines[i+1]:
                lines[i] += "    'livereload',\n    'rest_framework',\n"
                for app_name in app_names:
                    lines[i] += "    '"+app_name+"',\n"
            if "'django.middleware.clickjacking.XFrameOptionsMiddleware'," in lines[i] and 'livereload' not in lines[i+1]:
                lines[i] += "    'livereload.middleware.LiveReloadScript',\n"
            print(lines[i], i)
            try:    
                if lines[i].startswith("STATIC_URL = ") and not lines[i+1].startswith("STATICFILES_DIRS"):
                    lines[i] += "STATICFILES_DIRS = [STATIC_DIR,]\n\
\n\
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')\n\
MEDIA_URL = '/media/'\n\
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')\n\
\n\
LOGIN_REDIRECT_URL = 'index'\n\
LOGOUT_REDIRECT_URL = 'index'\n\
LOGIN_URL = 'user_login'\n"
            except:
                lines[i] += "STATICFILES_DIRS = [STATIC_DIR,]\n\
\n\
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')\n\
MEDIA_URL = '/media/'\n\
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')\n\
\n\
LOGIN_REDIRECT_URL = 'index'\n\
LOGOUT_REDIRECT_URL = 'index'\n\
LOGIN_URL = 'user_login'"
            f.write(str(lines[i]))
    f.write('\n')
    f.close()

    # INSTALLED APPS, livereload, rest_framework

    if 'accounts' in app_names:

        content += "\nAUTH_USER_MODEL = 'accounts.Account'\n"
 

    shutil.copy(proj_name+'/settings_new.py', proj_name+'/settings.py')    
    

if __name__ == '__main__':
    settings_project()