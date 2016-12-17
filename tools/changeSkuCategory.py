import requests
import os
from datetime import timedelta, datetime
import itertools

download_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=OPEN'
upload_hdfs_api = 'http://10.10.129.142:14000/webhdfs/v1%s?user.name=mercury&op=CREATE&data=true&overwrite=true'


def _to_partition_name(partition):
    return 'part-' + '%05d' % partition

def _download_file(remote_path, local_path):
    resp = requests.get(download_hdfs_api % remote_path)
    if resp.status_code == 200:
        with open(local_path, 'wb') as local_file:
            local_file.write(resp.content)
    return os.path.exists(local_path)

def _is_exist_file(remote_path):
    resp = requests.get(download_hdfs_api % remote_path)
    return resp.status_code == 200

def _download_sku_category_file(date, file_name):
    hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/%s/' % date
    remote_path = hdfs_path + file_name
    print(remote_path)
    if _is_exist_file(remote_path):
        local_path = '../work_dir/' + file_name + date
        _download_file(remote_path, local_path)

def _date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n + 1)

def _download():
    end_date = datetime.today()
    start_date = datetime.today() - timedelta(15)
    count = 0
    for single_date in _date_range(start_date, end_date):
        print(single_date.strftime("%Y%m%d"))
        _download_sku_category_file(single_date.strftime("%Y%m%d"), 'sku_category')
    print(count)

def _change_sku_category_file(date, file_name, mydict):
    dist_file = '../work_dir/' + file_name + date
    writer_file = '../work_dir/' + file_name + date + 'new'
    reader2 = open(dist_file, 'r')
    writer = open(writer_file, 'w')
    for line in reader2:
        strs = line.split('$')
        if strs[0] not in mydict:
            writer.write(line[:-1] + '$22221231\n')
        else:
            writer.write(line[:-1] + '$' + mydict[strs[0]])

def _change():
    end_date = datetime.today()
    start_date = datetime.today() - timedelta(15)
    file_name = 'sku_category'
    source_file = '../work_dir/' + file_name
    reader1 = open(source_file, 'r')
    mydict = {}

    for line in reader1:
        strs = line.split('$')
        mydict[strs[0]] = strs[-1]
    for single_date in _date_range(start_date, end_date):
        print(single_date.strftime("%Y%m%d"))
        _change_sku_category_file(single_date.strftime("%Y%m%d"), file_name, mydict)

def upload_file(local_path, hdfs_path):
    data = open(local_path).read()
    resp = requests.put(
        url = upload_hdfs_api % (hdfs_path),
        data = data,
        headers = {'Content-Type': 'application/octet-stream'}
    )
    return resp.status_code == 201

def _upload_sku_category_file(date, file_name):
    local_path = '../work_dir/' + file_name + date + 'new'
    hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/%s/%s' % (date, file_name + '_new')
    upload_file(local_path, hdfs_path)

def _upload():
    end_date = datetime.today()
    start_date = datetime.today() - timedelta(15)
    for single_date in _date_range(start_date, end_date):
        print(single_date.strftime("%Y%m%d"))
        _upload_sku_category_file(single_date.strftime("%Y%m%d"), 'sku_category')


def main():
    #_download()
    _change()
    _upload()

    print()

if __name__ == '__main__':
    main()
