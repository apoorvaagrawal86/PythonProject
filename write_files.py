# file_one = open('textfile.txt', 'w')
# file_one.write('This is a new file to wriite text')
# file_one.close()

# file_two = open('ExcelFile.xls', 'w')
# file_two.write('This is a new excel file')
# file_two.close()

# with open('textfile2.txt', 'w') as demo_file:
#     demo_file.write('This is created using with as')

# with open('textfile2.txt', 'a') as demo_file:
#     demo_file.write('This is appended to the previous text')

# read_only = open('textfile.txt', 'r')
# print(read_only.read())

# read_only_excel = open('ExcelFile.xls', 'r')
# print(read_only_excel.read())

# with open('textfile2.txt', 'r') as read_file:
#     print(read_file.read())

with open('textfile2.txt', 'r') as read_line:
    print(read_line.readline())
    print(read_line.readline())