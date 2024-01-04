```bash
pip install boto3
```

```bash
# FRONTEND_TO_BACKEND_DELAY=0.1 #100ms
# BACKEND_TO_SCHEDULER_VIA_NATS_DELAY=3 #3s

# 4 files, 1.3MB
@ojjsaw ➜ /workspaces/s3-upload-download/upload-download-test (main) $ python backend.py 
INFO:root:Sequential - success_download_count: 4
INFO:root:Sequential - Elapsed time: 3.612931489944458 seconds
INFO:root:batch - success_download_count: 4
INFO:root:batch - Elapsed time: 4.205922365188599 seconds

# 200 files, 72MB
@ojjsaw ➜ /workspaces/s3-upload-download/upload-download-test (main) $ python backend.py 
INFO:root:Sequential - success_download_count: 200
INFO:root:Sequential - Elapsed time: 120.80737733840942 seconds
INFO:root:batch - success_download_count: 200
INFO:root:batch - Elapsed time: 50.43735718727112 seconds
```