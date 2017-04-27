workspace = '/Users/cindy.wang/Downloads/'

input_file = workspace + 'input.csv'
output_sales_file = workspace + 'sales.csv'
output_oos_file = workspace + 'oos.csv'


def main():
    count = 0
    writer_sales = open(output_sales_file, 'w')
    writer_oos = open(output_oos_file, 'w')
    with open(input_file, 'r') as reader:
        for line in reader:
            count += 1
            if count == 1:
                writer_oos.write(line.replace('"', ''))
                writer_sales.write(line.replace('"', ''))
            else:
                strs = line.split(',')
                temp_oos = []
                temp_sales = []
                for i in range(0, len(strs)):
                    strs[i] = strs[i].replace('"', '')
                    if ';' in strs[i]:
                        (sales, inventory, oos) = strs[i].split(';')
                        temp_oos.append(oos)
                        temp_sales.append(sales)
                    elif strs[i] == '':
                        temp_oos.append('NA')
                        temp_sales.append('NA')
                    else:
                        temp_oos.append(strs[i])
                writer_oos.write(','.join(temp_oos))
                writer_sales.write(','.join(temp_sales))




if __name__ == '__main__': main()