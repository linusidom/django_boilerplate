import os
import shutil

def settings_project(app_name, dst, proj_name):
    auth_model = 0
    installad_apps = 0
    middleware_apps = 0
    arr = []

    if 'accounts' in app_name:
        auth_model = 1

    src_proj_files = '/Users/Admin/coding/django/django_create_base/proj_files'

    # Copy the settings file from the project directory to another settings file in the same project directory
    
    shutil.copy(proj_name+'/settings.py', proj_name+'/settings_orig.py')

    f = open(proj_name + '/settings_orig.py','r')
    contents = f.readlines()
    f.close()

    # if contents[-1] == '#updated':
    #     print('Settings already updated')
    #     return
    
    # "TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')"
    # "STATIC_DIR = os.path.join(BASE_DIR, 'static')"
    # "'DIRS': [TEMPLATE_DIR,],"
    if '#updated' not in contents[-1]:    
        for i in range(len(contents)):
            if "BASE_DIR = " in contents[i]:
                contents[i] += "TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')\n\
STATIC_DIR = os.path.join(BASE_DIR, 'static')\n"
            if "'DIRS': []," in contents[i]:
                contents[i] = "        'DIRS': [TEMPLATE_DIR,],\n"
            if "AUTH_USER_MODEL =" in contents[i]:
                auth_model = 0

    # INSTALLED_APPS
    for i in range(len(contents)):
        if "INSTALLED_APPS" in contents[i]:
            installad_apps = 1
            start_installed_index = i + 1
        elif ']' in contents[i] and installad_apps:
            installad_apps = 0
            end_installed_index = i
        
    for i in range(start_installed_index, end_installed_index):
        contents[i] = contents[i].strip().replace("\',",'').replace("'",'')
        arr.append(contents[i])
    if 'livereload' not in arr:
        arr.append('livereload')
    if 'rest_framework' not in arr:
        arr.append('rest_framework')
    for app in app_name:
        if app not in arr:
            arr.append(app)
        

    del contents[start_installed_index - 1:end_installed_index+1]
    j = 0
    contents.insert(start_installed_index - 1, "INSTALLED_APPS = [\n")
    # for i in range(start_installed_index, end_installed_index + len(app_name)):
    
    for j in range(len(arr)-1, -1, -1):
        if arr[j] != '':
            contents.insert(start_installed_index,"    '"+arr[j]+"',\n")
        if j == 0:
            contents.insert(start_installed_index + len(arr), ']\n')
    if auth_model:
        contents.insert(start_installed_index + len(arr) + 1, "\nAUTH_USER_MODEL = 'accounts.Account'\n")
  
   





    # # MIDDLEWARE
    # 'livereload.middleware.LiveReloadScript'
    

    for i in range(len(contents)):
        if "MIDDLEWARE = [" in contents[i]:
            middleware_apps = 1
            start_middleware_index = i + 1
        elif ']' in contents[i] and middleware_apps:
            middleware_apps = 0
            end_middleware_index = i
    arr = []
    for i in range(start_middleware_index, end_middleware_index):
        contents[i] = contents[i].strip().replace("\',",'').replace("'",'')
        # print('**', contents[i])
        arr.append(contents[i])
    if 'livereload.middleware.LiveReloadScript' not in arr:
        arr.append('livereload.middleware.LiveReloadScript')

    del contents[start_middleware_index - 1:end_middleware_index+1]
    j = 0
    contents.insert(start_middleware_index - 1, "MIDDLEWARE = [\n")
    for j in range(len(arr)-1, -1, -1):
        if arr[j] != '':  
            contents.insert(start_middleware_index,"    '"+arr[j]+"',\n")
    contents.insert(start_middleware_index + len(arr), ']\n')


    # END of FILE Appends
    if '#updated' not in contents[-1]:    
        contents.insert(len(contents), "STATICFILES_DIRS = [STATIC_DIR,]\n\
\n\
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')\n\
MEDIA_URL = '/media/'\n\
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')\n\
\n\
LOGIN_URL = 'user_login'\n\
LOGIN_REDIRECT_URL = 'index'\n\
LOGOUT_REDIRECT_URL = 'index'\n\
#updated DO NOT REMOVE THIS LINE - IF REMOVED IT WILL BREAK UPDATES")
    
    f = open(proj_name + '/settings.py', 'w')
    for line in contents:
        # print(line)
        f.write(line)
    f.close()


# if __name__ == '__main__':
#     settings_project(app_name = ['accounts', 'campaigns'],dst='/', proj_name='test_bidding')