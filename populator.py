import numpy as np
import time
from openpyxl import Workbook
import pandas as pd
##arr = np.zeros((5,5))
##limit = arr.shape[0]
##row_range = np.arange(0, limit)
##for n, row in enumerate(arr):
##    for cell in row_range:
##        arr[n, cell] = (cell + 1)**n
##print(row_range)

def populate_array(arr_shape:tuple):
    arr = np.zeros(arr_shape)
    limit = arr.shape[0]
    row_range = np.arange(0, limit)
    for n, row in enumerate(arr):
        for cell in row_range:
            arr[n, cell] = (cell+1)**(n+1)
    return arr

my_array = populate_array(arr_shape=(10,10))

def write_table(arr:np.array):
    wb = Workbook()
    ws = wb.active
    try:
        for row in arr:
            ws.append(list(row))
        wb.save('output/my_table.xlsx')
    except TypeError:
        print("Error: Invalid argument")

write_table(arr=my_array)


