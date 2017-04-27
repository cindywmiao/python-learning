import requests
import os
import utils.logging_util as logging
logger = logging.get_logger(__name__)

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'
delete_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=DELETE'
upload_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=CREATE&data=true&overwrite=true'

def download_file(remote_path, local_path):
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    if not os.path.exists(local_path):
        logger.error('download from hdfs failed %s' % remote_path)
    return os.path.exists(local_path)

def upload_file(local_path, hdfs_path):
    data = open(local_path).read()
    resp = requests.put(
        url = upload_hdfs_api % (hdfs_path),
        data = data,
        headers = {'Content-Type': 'application/octet-stream'}
    )
    return resp.status_code ==  201

def is_exist_file(remote_path):
    resp = requests.get(download_hdfs_api % remote_path)
    return resp.status_code == 200

def delete_file(remote_path):
    if is_exist_file(remote_path):
        resp = requests.put(
            url = delete_hdfs_api % (remote_path),
            data = None,
            headers = {'Content-Type': 'application/octet-stream'}
        )
        print('Here')
        print(resp.status_code)
        return resp.status_code == 200

