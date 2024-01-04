from urllib.parse import urlparse, unquote
import requests
import os
import requests
import logging
def find_image_files_and_store_paths(directory):
    local_file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                local_file_paths.append(file_path)
    return local_file_paths

def preprocess_objects_to_keys(local_file_paths, target_s3_prefix_dir, local_upload_dir):
    upload_s3_keys = []
    for local_path in local_file_paths:
        upload_s3_keys.append(os.path.join(target_s3_prefix_dir, os.path.relpath(local_path, local_upload_dir)))
    return upload_s3_keys

def upload_file_to_s3(pre_signed_url, file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.put(pre_signed_url, data=file)
            if response.status_code == 200:
                return True
            else:
                logging.info(f"Failed to upload file. Status code: {response.status_code}")
                return False
    except Exception as ex:
        logging.error(f"Error: {str(ex)}")
        return False

def download_file_from_s3(pre_signed_url, local_base_directory):
    try:
        response = requests.get(pre_signed_url)
        if response.status_code == 200:
            # Extract the relative path from the pre-signed URL
            parsed_url = urlparse(pre_signed_url)   
            # Extract the path component and decode any URL-encoded characters
            file_path = unquote(parsed_url.path)
            file_path = file_path.lstrip('/')
            full_path = os.path.join(local_base_directory, file_path)
            directory = os.path.dirname(full_path)
            os.makedirs(directory, exist_ok=True)
            with open(full_path, 'wb') as file:
                file.write(response.content)         
            return True
        else:
            logging.info(f"Failed to download file. Status code: {response.status_code}")
            return False
    except Exception as ex:
        logging.error(f"Error: {str(ex)}")
        return False

