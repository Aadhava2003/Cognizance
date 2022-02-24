#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Home
#
# Created:     23-02-2022
# Copyright:   (c) Home 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = int(input("Enter the number of rows:"))
m = (n*2)-2
for i in range(0,n):
    for j in range(0,m):
        print(end=" ")
    m = m - 1
    for j in range(0,i+1):
        print("*",end=" " )
    print(" ")