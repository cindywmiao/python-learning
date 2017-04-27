from datetime import datetime
import string

workspace = '/Users/cindy.wang/Downloads/'

def _has_interval(start_date1, start_date2, end_date1, end_date2):
    if start_date1 > end_date2 :
        return False
    elif start_date2 > end_date1 :
        return False
    else:
        return True


def main():
    print('main')
    outlet_history_path = workspace + 'outlet_history.csv'
    seasonal_peak_path = workspace + 'seasonal_peak.csv'

    reader_outlet = open(outlet_history_path, 'r')
    reader_seasonal = open(seasonal_peak_path, 'r')

    writer = open(workspace + 'result.csv', 'w')
    writer.write('skuId' + ',' + 'outlet_history:start_date' + ',' + 'outlet_history:end_date' + ',' +
                 'seasonal_peak:start_date' + ',' + 'seasonal_peak:end_date2' + '\n')

    mydict = {}

    for line in reader_seasonal:
        strs = line.split(',')
        sku = unicode(strs[2], 'utf-8')
        if sku.isnumeric():
            start_date = datetime.strptime(strs[3], "%Y%m%d")
            end_date = datetime.strptime(strs[4], "%Y%m%d")
            mydict[sku] = (start_date, end_date, line)

    result = {}

    for line in reader_outlet:
        strs = line.split(',')
        sku = unicode(strs[0], 'utf-8')
        if sku.isnumeric():
            start_date2 = datetime.strptime(strs[1], "%Y-%m-%d")
            end_date2 = datetime.strptime(strs[2][:-1], "%Y-%m-%d")

            # if sku not in mydict:
            #     #(start_date1, end_date1) = mydict[sku]
            #     # if _has_interval(start_date1, start_date2, end_date1, end_date2):
            #     writer.write(line)
            #     # writer.write(sku + ',' +
            #     #     start_date1.strftime("%Y%m%d") + ',' + end_date1.strftime("%Y%m%d") + ',' +
            #     #     start_date2.strftime("%Y%m%d") + ',' + end_date2.strftime("%Y%m%d") + '\n')
            if sku in mydict:
                del mydict[sku]

    for sku in mydict:
        (start_date, end_date, line)  = mydict[sku]
        writer.write(line)




if __name__ == '__main__' : main()