import os
import utils as util
from datetime import timedelta, datetime

workspace = '/Users/cindy.wang/Downloads/forecast/'
hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/children-holiday/'


def valide(target_date):
    os.mkdir(workspace + target_date)
    remote_file = hdfs_path + target_date + '/result-21-days-national.csv'
    local_file = workspace + target_date + '/output.csv'
    util.download_file(remote_file, local_file)

    with open(local_file, 'r') as reader:
        for line in reader:
            strs = line.split(',')
            if len(strs) != 57:
                print(line)

def main():
    start_date = datetime.strptime('20170416', '%Y%m%d')
    for i in range(0, 1):
        target_date = start_date + timedelta(days = i)
        valide(target_date.strftime('%Y%m%d'))

if __name__ == '__main__': main()