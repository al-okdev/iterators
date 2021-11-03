import hashlib


def generators_md5(path):
    file = open(path)
    while file.readline():
        yield hashlib.md5(file.readline().encode('utf-8')).hexdigest()


if __name__ == '__main__':
    for item_str in generators_md5('result.txt'):
        print(item_str)
