'''file=open("data.txt",mode='r')
with open("data.txt",mode='r') as file:
    for line in file:
        print(line)'''

'''import linecache
line_number=3
line=linecache.getline("data.txt",line_number)
print(f"line number is {line_number} and the line is: {line}")'''

with open("data.txt",mode='r') as file:
    f=file.readlines()
    for line in f:
        print (line.strip().split(":")[0])
