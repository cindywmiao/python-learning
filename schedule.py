

def main():
    print('main')
    input_file = '/Users/cindy.wang/Downloads/schedule.csv'
    reader = open(input_file, 'r')
    for line in reader:
        if 'DEPJOB' in line or 'yliu' in line:
            date = line[0: 10]
            start_time = line[11: 20]
            end_time = line[31: 40]
            duration = line[40:].split("	")[0]
            result = """<tr>
                      <td colspan="1">%s</td>
                      <td colspan="1">%s</td>
                      <td colspan="1">%s</td>
                      <td colspan="1">%s</td>
                      <td colspan="1">
                        <span>v1.0.4</span>
                      </td>
                    </tr>""" % (date, start_time, end_time, duration)
            print(result)


if __name__ == '__main__':
    main()