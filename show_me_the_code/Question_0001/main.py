import random
import string

field = string.letters + string.digits

def getRandom():
    return "".join(random(field, 4))


def gene_code(group):
    return "-".join([getRandom() for i in range(group)])

def generate(n):
    return [gene_code(4) for i in range(n)]

if __name__ == '__main__':
    print generate(20)