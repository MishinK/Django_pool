#coding=utf8
def numbers():
    with open('numbers.txt', 'r') as fd:
        str_nbr = fd.read()
    lst_nbr = str_nbr.replace('\n', '').split(',')
    for nbr in lst_nbr:
        print(nbr)

if __name__ == '__main__':
    numbers()