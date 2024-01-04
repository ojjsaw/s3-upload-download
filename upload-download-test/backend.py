import os
import shutil
import time
import logging
from s3_utils import S3Utils
from sim_utils import preprocess_objects_to_keys, find_image_files_and_store_paths, upload_file_to_s3, download_file_from_s3

EXPIRY_TIME=1800 # 30mins
ACCESS_KEY='AKIA4UQN57YSYG4VU3ND'
SECRET_KEY='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'
BUCKET_NAME='s3-upload-download-test2'
LOCAL_UPLOAD_DIR='/workspaces/s3-upload-download/upload-download-test/mini-upload-test'
TARGET_S3_PREFIX_DIR='cache'
logging.basicConfig(level=logging.INFO)

def sequential_upload_download():
    
    download_dir = '/workspaces/s3-upload-download/upload-download-test/sequential-download'
    local_file_paths = find_image_files_and_store_paths(LOCAL_UPLOAD_DIR)
    upload_s3_keys = preprocess_objects_to_keys(local_file_paths, TARGET_S3_PREFIX_DIR, LOCAL_UPLOAD_DIR)

    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    s3_utils = S3Utils(BUCKET_NAME, ACCESS_KEY, SECRET_KEY)

    start_time = time.time()

    success_upload_count = 0
    success_download_count = 0
    for index, local_path in enumerate(local_file_paths):
        presigned_download_url, presigned_download_url = None, None
        upload_success, download_success = False, False

        presigned_upload_url = s3_utils.generate_presigned_upload_url(upload_s3_keys[index])
        if presigned_upload_url is not None:
           upload_success = upload_file_to_s3(presigned_upload_url, local_path)

        if upload_success:
            success_upload_count += 1
            presigned_download_url = s3_utils.generate_presigned_download_url(upload_s3_keys[index])
        
        if presigned_download_url is not None:
            download_success = download_file_from_s3(presigned_download_url, download_dir)

        if download_success:
            success_download_count += 1

    end_time = time.time()

    logging.info(f"Sequential - success_upload_count: {str(success_upload_count)}")
    logging.info(f"Sequential - success_download_count: {str(success_download_count)}")

    s3_utils.delete_all_data_s3(TARGET_S3_PREFIX_DIR)

    elapsed_time = end_time - start_time
    logging.info(f"Sequential - Elapsed time: {elapsed_time} seconds")


def batch_upload_download():
    
    download_dir = '/workspaces/s3-upload-download/upload-download-test/batch-download'
    local_file_paths = find_image_files_and_store_paths(LOCAL_UPLOAD_DIR)
    upload_s3_keys = preprocess_objects_to_keys(local_file_paths, TARGET_S3_PREFIX_DIR, LOCAL_UPLOAD_DIR)

    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    s3_utils = S3Utils(BUCKET_NAME, ACCESS_KEY, SECRET_KEY)

    start_time = time.time()

    success_upload_count = 0
    success_download_count = 0

    presigned_upload_urls = []
    presigned_download_urls = []

    for index, local_path in enumerate(local_file_paths):
        presigned_upload_url = s3_utils.generate_presigned_upload_url(upload_s3_keys[index])
        presigned_upload_urls.append(presigned_upload_url)
    
    for index, local_path in enumerate(local_file_paths):
        if presigned_upload_url is not None:
            upload_success = upload_file_to_s3(presigned_upload_urls[index], local_path)
            if upload_success:
                success_upload_count += 1

    for index, local_path in enumerate(local_file_paths):
        presigned_download_url = s3_utils.generate_presigned_download_url(upload_s3_keys[index])
        presigned_download_urls.append(presigned_download_url)

    for index, local_path in enumerate(local_file_paths):
        if presigned_download_url is not None:
            download_success = download_file_from_s3(presigned_download_urls[index], download_dir)
            if download_success:
                success_download_count += 1

    end_time = time.time()

    logging.info(f"batch - success_upload_count: {str(success_upload_count)}")
    logging.info(f"batch - success_download_count: {str(success_download_count)}")

    s3_utils.delete_all_data_s3(TARGET_S3_PREFIX_DIR)

    elapsed_time = end_time - start_time
    logging.info(f"batch - Elapsed time: {elapsed_time} seconds")

sequential_upload_download()
batch_upload_download()
