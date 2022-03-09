#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aadhava
#
# Created:     09-03-2022
# Copyright:   (c) Home 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def areEqual(arr1,arr2,n,m):

    if (n != m):
        return False
    b1 = arr1[0]
    b2 = arr2[0]
    for i in range(1,n-1):
        b1= arr1[i]
    for i in range(1,m-1):
        b2= arr2[i]
    all_xor=b1^b2
    if(all_xor == 0):
        return True
    return False
arr1 = [6,0,2,0,0]
arr2 = [6,5,5,7,2]
n = len(arr1)
m = len(arr2)
if (areEqual(arr1, arr2, n, m)):
    print("True")
else:
    print("False")