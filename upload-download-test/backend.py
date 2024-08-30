import os
import shutil
import time
import logging
import concurrent.futures
from s3_utils import S3Utils
from sim_utils import preprocess_objects_to_keys, find_image_files_and_store_paths, upload_file_to_s3, download_file_from_s3

EXPIRY_TIME=1800 # 30mins
ACCESS_KEY=''
SECRET_KEY=''
BUCKET_NAME='s3-upload-download-test2'
LOCAL_UPLOAD_DIR='/workspaces/s3-upload-download/upload-download-test/data-to-upload'
TARGET_S3_PREFIX_DIR='cache'
logging.basicConfig(level=logging.INFO)
FRONTEND_TO_BACKEND_DELAY=0.1 #100ms
BACKEND_TO_SCHEDULER_VIA_NATS_DELAY=3 #3s

def process_file(index, local_path, s3_utils, upload_s3_keys, download_dir):
    presigned_upload_url = s3_utils.generate_presigned_upload_url(upload_s3_keys[index])
    time.sleep(FRONTEND_TO_BACKEND_DELAY)
    if presigned_upload_url is not None:
        upload_success = upload_file_to_s3(presigned_upload_url, local_path)
        if upload_success:
            presigned_download_url = s3_utils.generate_presigned_download_url(upload_s3_keys[index])
            time.sleep(FRONTEND_TO_BACKEND_DELAY)
            if presigned_download_url is not None:
                time.sleep(BACKEND_TO_SCHEDULER_VIA_NATS_DELAY)
                download_success = download_file_from_s3(presigned_download_url, download_dir)
                if download_success:
                    return 1
    return 0

def sequential_upload_download():
    
    download_dir = '/workspaces/s3-upload-download/upload-download-test/results-seq-download'
    local_file_paths = find_image_files_and_store_paths(LOCAL_UPLOAD_DIR)
    upload_s3_keys = preprocess_objects_to_keys(local_file_paths, TARGET_S3_PREFIX_DIR, LOCAL_UPLOAD_DIR)

    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    s3_utils = S3Utils(BUCKET_NAME, ACCESS_KEY, SECRET_KEY)

    start_time = time.time()

    success_upload_count = 0
    success_download_count = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, index, local_path, s3_utils, upload_s3_keys, download_dir)
                for index, local_path in enumerate(local_file_paths)]

        for future in concurrent.futures.as_completed(futures):
            success_download_count += future.result()

    end_time = time.time()

    logging.info(f"Sequential - success_download_count: {str(success_download_count)}")

    s3_utils.delete_all_data_s3(TARGET_S3_PREFIX_DIR)

    elapsed_time = end_time - start_time
    logging.info(f"Sequential - Elapsed time: {elapsed_time} seconds")


def download_file(index, presigned_url, download_dir):
    try:
        if presigned_url is not None:
            download_success = download_file_from_s3(presigned_url, download_dir)
            if download_success:
                return 1
    except Exception as e:
        print(f"Error downloading file {index}: {str(e)}")
    return 0

def batch_upload_download():
    
    download_dir = '/workspaces/s3-upload-download/upload-download-test/results-batch-download'
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
    time.sleep(FRONTEND_TO_BACKEND_DELAY)
    
    for index, local_path in enumerate(local_file_paths):
        if presigned_upload_url is not None:
            upload_success = upload_file_to_s3(presigned_upload_urls[index], local_path)
            if upload_success:
                success_upload_count += 1

    for index, local_path in enumerate(local_file_paths):
        presigned_download_url = s3_utils.generate_presigned_download_url(upload_s3_keys[index])
        presigned_download_urls.append(presigned_download_url)
    time.sleep(FRONTEND_TO_BACKEND_DELAY)

    time.sleep(BACKEND_TO_SCHEDULER_VIA_NATS_DELAY)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(download_file, range(len(local_file_paths)), presigned_download_urls, [download_dir]*len(local_file_paths)))

    success_download_count = sum(results)

    # for index, local_path in enumerate(local_file_paths):
    #     if presigned_download_url is not None:
    #         download_success = download_file_from_s3(presigned_download_urls[index], download_dir)
    #         if download_success:
    #             success_download_count += 1

    end_time = time.time()

    logging.info(f"batch - success_download_count: {str(success_download_count)}")

    s3_utils.delete_all_data_s3(TARGET_S3_PREFIX_DIR)

    elapsed_time = end_time - start_time
    logging.info(f"batch - Elapsed time: {elapsed_time} seconds")

sequential_upload_download()
batch_upload_download()
