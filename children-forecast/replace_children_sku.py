import utils as util
import csv
from datetime import timedelta, datetime
import os

workspace = '/Users/cindy.wang/Downloads/Archive/'
hdfs_path = '/user/mercury/scm-output/scm_forecast_demand_forecast/'

title = 'sku,mean_of_next_7_days,unit,category,mean_d1,mean_d2,mean_d3,mean_d4,mean_d5,mean_d6,mean_d7,mean_d8,mean_d9,mean_d10,mean_d11,mean_d12,mean_d13,mean_d14,mean_d15,mean_d16,mean_d17,mean_d18,mean_d19,mean_d20,mean_d21,std_d1,std_d2,std_d3,std_d4,std_d5,std_d6,std_d7,std_d8,std_d9,std_d10,std_d11,std_d12,std_d13,std_d14,std_d15,std_d16,std_d17,std_d18,std_d19,std_d20,std_d21,area,sku_class,sku_status,recent_28_days_mean,recent_28_days_std,model_type,eligible_days,outlet_days,seasonal_peak_days,oos_days,outlier_days\n'


def generate_child_sku_forecast(target_date):
    file_name =  workspace + 'child.sku.' + target_date + '.forecast.csv'
    result = {}
    with open(file_name, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['skuseq'] not in result:
                result[row['skuseq']] = {}
            result[row['skuseq']][row['date']] = row['forecast']

    output_file = workspace + 'child.sku.output.' + target_date + '.forecast.csv'
    writer = open(output_file, 'w')

    for key, value in result.items():
        start_date = datetime.strptime(target_date, '%Y-%m-%d')
        writer.write(key)
        for i in range(0, 21):
            current_date = start_date + timedelta(days=i)
            current_date_string = current_date.strftime('%Y-%m-%d')
            if current_date_string in value:
                writer.write(',' + "%.2f" % float(value[current_date_string]))
            else:
                writer.write(',' + '0')
        writer.write('\n')


def row_to_string(row):
    res = []
    res.append(row['sku'])
    res.append(row['mean_of_next_7_days'])
    res.append(row['unit'])
    res.append(row['category'])
    res.append(row['mean_d1'])
    res.append(row['mean_d2'])
    res.append(row['mean_d3'])
    res.append(row['mean_d4'])
    res.append(row['mean_d5'])
    res.append(row['mean_d6'])
    res.append(row['mean_d7'])
    res.append(row['mean_d8'])
    res.append(row['mean_d9'])
    res.append(row['mean_d10'])
    res.append(row['mean_d11'])
    res.append(row['mean_d12'])
    res.append(row['mean_d13'])
    res.append(row['mean_d14'])
    res.append(row['mean_d15'])
    res.append(row['mean_d16'])
    res.append(row['mean_d17'])
    res.append(row['mean_d18'])
    res.append(row['mean_d19'])
    res.append(row['mean_d20'])
    res.append(row['mean_d21'])
    res.append(row['std_d1'])
    res.append(row['std_d2'])
    res.append(row['std_d3'])
    res.append(row['std_d4'])
    res.append(row['std_d5'])
    res.append(row['std_d6'])
    res.append(row['std_d7'])
    res.append(row['std_d8'])
    res.append(row['std_d9'])
    res.append(row['std_d10'])
    res.append(row['std_d11'])
    res.append(row['std_d12'])
    res.append(row['std_d13'])
    res.append(row['std_d14'])
    res.append(row['std_d15'])
    res.append(row['std_d16'])
    res.append(row['std_d17'])
    res.append(row['std_d18'])
    res.append(row['std_d19'])
    res.append(row['std_d20'])
    res.append(row['std_d21'])
    res.append(row['area'])
    res.append(row['sku_class'])
    res.append(row['sku_status'])
    res.append(row['recent_28_days_mean'])
    res.append(row['recent_28_days_std'])
    res.append(row['model_type'])
    res.append(row['eligible_days'])
    res.append(row['outlet_days'])
    res.append(row['seasonal_peak_days'])
    res.append(row['oos_days'])
    res.append(row['outlier_days'])
    return ",".join(res) + '\n';

def row_to_string_with_child_forecast(row, child_forecast_dict):
    forecast = child_forecast_dict[row['sku']]
    strs = forecast.split(',')
    sum = 0
    for i in range(0, 7):
        sum += float(strs[i])
    mean_7_days_forecast = sum / 7
    res = []
    res.append(row['sku'])
    res.append(str(mean_7_days_forecast))
    res.append(row['unit'])
    res.append(row['category'])
    res.append(forecast)
    res.append(row['std_d1'])
    res.append(row['std_d2'])
    res.append(row['std_d3'])
    res.append(row['std_d4'])
    res.append(row['std_d5'])
    res.append(row['std_d6'])
    res.append(row['std_d7'])
    res.append(row['std_d8'])
    res.append(row['std_d9'])
    res.append(row['std_d10'])
    res.append(row['std_d11'])
    res.append(row['std_d12'])
    res.append(row['std_d13'])
    res.append(row['std_d14'])
    res.append(row['std_d15'])
    res.append(row['std_d16'])
    res.append(row['std_d17'])
    res.append(row['std_d18'])
    res.append(row['std_d19'])
    res.append(row['std_d20'])
    res.append(row['std_d21'])
    res.append(row['area'])
    res.append(row['sku_class'])
    res.append(row['sku_status'])
    res.append(row['recent_28_days_mean'])
    res.append(row['recent_28_days_std'])
    res.append(row['model_type'])
    res.append(row['eligible_days'])
    res.append(row['outlet_days'])
    res.append(row['seasonal_peak_days'])
    res.append(row['oos_days'])
    res.append(row['outlier_days'])
    return ",".join(res) + '\n'


def replace(target_date):
    generate_child_sku_forecast(target_date)
    local_file = workspace + target_date + '_result-21-days-national.csv'
    remote_file = hdfs_path + datetime.strptime(target_date, '%Y-%m-%d').strftime('%Y%m%d') + '/result-21-days-national-raw.csv'
    util.download_file(remote_file, local_file)

    child_forecast_result = workspace + 'child.sku.output.' + target_date + '.forecast.csv'
    child_forecast_dict = {}
    with open(child_forecast_result, 'r') as reader:
        for line in reader:
            strs = line.split(',')
            sku = strs[0]
            forecast = line[len(sku) + 1:-1]
            child_forecast_dict[sku] = forecast

    writer = open(workspace + target_date + '_result.csv', 'w')
    writer.write(title)

    with open(local_file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # if row['sku'] == '655886':
            if row['sku'] not in child_forecast_dict:
                writer.write(row_to_string(row))
            else:
                writer.write(row_to_string_with_child_forecast(row, child_forecast_dict))    #print(row['sku'])

def main():
    start_date = datetime.strptime('20170416', '%Y%m%d')
    for i in range(0, 1):
        target_date = start_date + timedelta(days = i)
        replace(target_date.strftime('%Y-%m-%d'))

if __name__ == '__main__': main()