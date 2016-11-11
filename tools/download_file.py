import requests
import os

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'

def download_file(remote_path, local_path):
    print("download")
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    if not os.path.exists(local_path):
        print('download from hdfs failed %s' % remote_path)
    return os.path.exists(local_path)

todayDt = "20161110"
part = "00000"
download_path = "/user/mercury/scm-output/scm_forecast_demand_forecast/%s/part-%s" % (todayDt, part)
local_path = "/Users/cindy.wang/Workplace/python-learning/work_dir//%s/%s" % (todayDt, part)

download_file(download_path, local_path)