with open('C:/Users/hp/Desktop/python/read.txt','r') as file:
    header = file.readline().strip().split(',')
    footer = [i.split(',') for i in file.read().splitlines()]
    print(header,footer)