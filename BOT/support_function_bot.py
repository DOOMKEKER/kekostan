import os
import requests
import shutil


def safe_files(file, file_name, user_id):
    
    if not os.path.isdir(f'user_files/{user_id}'):
        os.mkdir(f'user_files/{user_id}')
    src = f'user_files/{user_id}/{file_name}'
    with open(src, 'wb') as new_file:
        new_file.write(file)


def send_files_to_api(file_list, user_id, key):
    
    files = {}

    url = "http://212.109.192.158/pdfun/api/v1.0/save_file_from_tg"

    for items in file_list:
        file = open(f'user_files/{user_id}/{items}', 'rb')
        print(key)
        multiple_files = [
            (str(key),(file)),
        ]
        requests.post(url, files=multiple_files)
        file.close()
        shutil.rmtree(f'user_files/{user_id}')

    
        
