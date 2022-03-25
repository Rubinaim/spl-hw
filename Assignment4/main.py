from Repository import repo
from DTOs import *
import sys


def config_file():
    with open(sys.argv[1]) as config:
        n = config.readline()
        n1 = n[:n.find(',')]
        n2 = n[n.find(',')+1:]
        i=0
        while i < int(n1):
            line = config.readline()
            coma1 = line.find(',')
            num = line[:coma1]
            coma2 = line.find(',', coma1+1)
            top = line[coma1+1:coma2]
            coma3 = line.find(',', coma2+1)
            sup = line[coma2+1:coma3]
            if line[-1] == '\n':
                quan = line[coma3+1:-1]
            else:
                quan = line[coma3+1:]
            repo.hats.insert(Hat(num, top, sup, quan))
            i = i+1
        j = 0
        while j < int(n2):
            line = config.readline()
            tmp = line.split(',')
            num = tmp[0]
            if tmp[1][-1] == '\n':
                name = tmp[1][:-1]
            else:
                name = tmp[1]
            repo.suppliers.insert(Supplier(num, name))
            j = j + 1


def orders_file():
    id = 1
    with open(sys.argv[3], 'w') as summary:
        with open(sys.argv[2], 'r') as orders:
            for line in orders:
                tmp = line.split(',')
                loc = tmp[0]
                if tmp[1][-1]=='\n':
                    top = tmp[1][0:-1]
                else:
                    top = tmp[1]
                hat = repo.hats.get_hat(top)
                if hat.id != 0:
                    repo.orders.insert(id, loc, hat.id)
                    summary.write(str(top)+','+str(repo.suppliers.get_supplier(hat.supplier).name)+','+str(loc)+'\n')
                    if hat.quantity > 1:
                        repo.hats.update(hat.id)
                    elif hat.quantity == 1:
                        repo.hats.delete(hat.id)
                    id = id + 1


def main():
    config_file()
    orders_file()


if __name__ == '__main__':
    main()
