
def main():
    print('Hello World')
    input_file = open('kITCHENSKU.csv', 'r')
    output_file = open('sku_category_new', 'w')

    for line in input_file:
        str = line.replace(',', '$')
        output_file.write(str[:-1])


if __name__ == '__main__':
    main()