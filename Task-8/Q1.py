import numpy as np

def zeroInsert(first_term,last_term,elements,zeros):

    user_arr = np.linspace(first_term, last_term, elements)
    return_arr = np.zeros(len(user_arr)+(len(user_arr)-1)*zeroes)
    return_arr[::no_of_zeroes+1] = user_arr
    return return_arr


first_term=int(input("Enter the first of the array - "))
last_term=int(input("Enter the last of the array - "))
no_of_elements=int(input("How many numbers to be found (inclusive) - "))
no_of_zeros=int(input("Enter the number of zeroes  - "))
print(zeroInsert(f_term, l_term, no_of_elements, no_of_zeroes))
