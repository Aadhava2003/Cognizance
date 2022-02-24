
def addInfo(size):

    data=[[],[],[]]
    rollno=data[0]
    names=data[1]
    marks=data[2]

    for i in range(size):
        stu_roll = input("Enter the roll no. - ")
        rollno.append(stu_roll)
        stu_name = input("Enter the name - ")
        names.append(stu_name)
        stu_mark = input("Enter the mark - ")
        marks.append(stu_mark)

    return data





def dispInfo(list_name, size):

    print('Roll no.  Name   marks')
    for j in range(size):
        print(list_name[0][j],'       ', list_name[1][j],'     ', list_name[2][j])

def searchInfo(list_name, roll_no, size):
    print('Roll no.  Name   marks')
    for j in range(size):
        if list_name[0][j] == roll_no:
            print(list_name[0][j], '       ', list_name[1][j], '     ', list_name[2][j])


size = int(input("Enter the size of the list - "))

return_list = addInfo(size)
dispInfo(return_list, size)

search_roll = input("Enter the roll no. to be searched : ")
searchInfo(return_list, search_roll, size)









