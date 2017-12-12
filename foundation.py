import os
import os.path
import sys

'''Select a file system you want to create'''
'''Flask, Frontend SASS, Front End CSS'''
base = '/home/trini7y/foundation_test';
os.chdir(base)

def css():
    css_file_folder=['styles', 'Javascript', 'images',]
    for folders in css_file_folder:
        change_dir = os.path.join(os.getcwd(), folders)
        if os.path.exists(change_dir):
            css_file_folder.remove(folders)
    return css_file_folder

def flask():
    flask_file_folders=['static', 'templates']
    for folders in flask_file_folders:
        change_dir = os.path.join(os.getcwd(), folders)
        if os.path.exists(change_dir):
            flask_file_folders.remove(folders)
    return flask_file_folders

# def scss():
#     def scss_subfolders():
#         scss_file_folders = ['base', 'components', 'helpers', 'layout', 'pages', 'themes', 'vendors']
#         for sub_folders in scss_file_folders:
#             # print(chdir)
#             change_dir = os.path.join(chdir, sub_folders)
#             if os.path.exists(change_dir):
#                 scss_file_folders.remove(sub_folders)
#         return scss_subfolders()
#     web_file_system = ['style', 'images', 'javascript']
#     # os.mkdir(web_file_system[0])
#     for folders in web_file_system:
#         os.chdir(folders[0:5])
#         change_folder = os.path.join(os.getcwd(), folders)
#         if os.path.exists(change_folder):
#             web_file_system.remove(folders)
#     return web_file_system



print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
make_new_directory = input("Enter the name of your project:  ")
file_name_input = input('Select  a file project file system: ')
new_dir = os.path.join(base, make_new_directory)

if not os.path.exists(new_dir):
    os.makedirs(new_dir, 0o777, True)
os.chdir(new_dir)
project_file_types = {'css':css(), 'flask':flask()}
project_file_types = {'css':css(), 'flask':flask()}
for key in project_file_types:
    for val in project_file_types[key]:
        directory = os.path.join(os.getcwd(), val)
        if file_name_input == key:
            if not os.path.exists(directory):
                os.makedirs(os.path.join(os.getcwd(), val))
