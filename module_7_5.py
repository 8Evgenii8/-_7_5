import os
import datetime

now = datetime.datetime.now()

path_ = (r'C:\Users\Пользователь\PycharmProjects\Project1\module_7')
for dirpath, dirnames, filenames in os.walk(path_):
    print(dirpath, dirnames, filenames)
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        formatted_time = now.strftime('%d.%m.%Y %H:%M')
        file_size = os.path.getsize(full_path)
        parent_dir = os.path.dirname(full_path)
        print(f'File: {filename}, '
              f'Modified: {formatted_time}'
              f', Size: {file_size} bytes, '
              f'Parent directory: {parent_dir}')