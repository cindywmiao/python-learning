import requests
import os

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'
upload_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=CREATE&data=true&overwrite=true'

def download_file(remote_path, local_path):
    """
    :param remote_path:
    :param local_path:
    :return:
    """
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    return os.path.exists(local_path)

def upload_file(local_path, hdfs_path):
    """
    :param local_path:
    :param hdfs_path:
    :return:
    """
    data = open(local_path).read()
    resp = requests.put(
        url = upload_hdfs_api %(hdfs_path),
        data = data,
        headers = {'Content-Type': 'application/octet-stream'}
    )
    return resp.status_code == 201

def is_exist_file(remote_path):
    """
    :param remote_path:
    :return:
    """
    resp = requests.get(download_hdfs_api % remote_path)
    return resp.status_code == 200