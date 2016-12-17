import requests
import os
from datetime import datetime

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'

def _to_partition_name(partition):
    return 'part-' + '%05d' % partition

def download_file(remote_path, local_path):
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    return os.path.exists(local_path)

def is_exist_file(remote_path):
    resp = requests.get(download_hdfs_api % remote_path)
    return resp.status_code == 200

def download_dir():
    partitions = 100
    hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/20161129/seoul/input/'
    for i in range(0, partitions):
        file_name = _to_partition_name(i)
        remote_path = hdfs_path + file_name
        if is_exist_file(remote_path):
            print('download')
            local_path = '../work_dir/' + file_name
            download_file(remote_path, local_path)

def main():
    download_dir()

if __name__ == '__main__':
    main()
