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

num=int(input("Enter the number:"))
rev=0
x=num
while(num>0):
    rev=(rev*10)+num%10
    num=num//10
if(x==rev):
     print("True")
else:
    print("False")
