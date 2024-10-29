import multiprocessing
from datetime import datetime

start_time = datetime.now()


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for i in file:
            all_data.append(i.strip())
    return all_data


# filenames = [f'file {number}.txt' for number in range(1, 5)]
# for name in filenames:
#     read_info(name)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=read_info, args=('file 1.txt',))
    process2 = multiprocessing.Process(target=read_info, args=('file 2.txt',))
    process3 = multiprocessing.Process(target=read_info, args=('file 3.txt',))
    process4 = multiprocessing.Process(target=read_info, args=('file 4.txt',))
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    end_time = datetime.now()
    res_time = end_time - start_time

    print(res_time)
