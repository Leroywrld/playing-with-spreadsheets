import numpy as np
from openpyxl import Workbook


def populate_array(arr_shape:tuple):
    '''This function takes an input in the form of a tuple that defines the shape of 
    the numpy array to be created.
    '''
    arr = np.zeros(arr_shape)
    limit = arr.shape[0]
    row_range = np.arange(0, limit)
    for n, row in enumerate(arr):
        for cell in row_range:
            arr[n, cell] = (cell+1)**(n+1)
    return arr

my_array = populate_array(arr_shape=(10,10))

def write_table(arr:np.array):
    '''this function writes the contents of the previously created
    numpy array to an excel through openpyxl'''
    wb = Workbook()
    ws = wb.active
    try:
        for row in arr:
            ws.append(list(row))
        wb.save('output/my_table.xlsx')
    except TypeError:
        print("Error: Invalid argument")

write_table(arr=my_array)


