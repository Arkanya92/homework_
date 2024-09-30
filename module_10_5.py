import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
'''
start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.datetime.now()
print(end - start)'''

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)




