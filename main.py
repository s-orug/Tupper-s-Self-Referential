#!/usr/bin/python3
import numpy as np
from pixel import Generator, Plotter, Tupper

__author__ = 'Sai Durga Rithvik Oruganti'
__date__ = 'Oct 14, 2022'
__email__ = 'orugants@email.sc.edu'
__status__ = 'Completed'


def flip(arr):
    for y_c, y in enumerate(arr):
        for x_c, x in enumerate(y):
            if x == 0:
                arr[y_c][x_c] = 1
            else:
                arr[y_c][x_c] = 0
    return arr


def main():
    x_range = 106
    y_range = 17


    k = Generator().main()
    count = 0
    b = np.array([[_ for _ in range(x_range)] for _ in range(y_range)])

    print(f'{k:,}')

    for y in range(16, -1, -1):
        for x in range(0, 106):
            b[y][x] = Tupper(k).tupper(x, y)
    if input('\nEnter yes or no to plot using the number above?\n').lower() in ['yes', 'y', '1']:
        Plotter(b[:, ::-1]).main()


if __name__ == '__main__':

    print(f'Created By   :  {__author__}')
    print(f'Created Date :  {__date__}')
    print(f'Email :  {__email__}')
    print(f'Status :  {__status__}\n')
    main()
