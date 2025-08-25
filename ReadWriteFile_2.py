from functionClause import total

f= open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r')
print(f.read())
f.close()

#print line by line
f= open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r')
for line in f:
    print(line)
f.close()

#convert in a list
f= open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r')
for line in f:
    tokens = line.split(' ')
    print(tokens)
f.close()

#count words in file
f= open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r')
for line in f:
    tokens = line.split(' ')
    print(len(tokens))

print(type(tokens))
f.close()

#write in a file the count of word per line
f= open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r')
f_out = open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny_wc.txt', 'w')

total=0
for line in f:
    tokens = line.split(' ')
    f_out.write(" wordcount: " +str(len(tokens))+" "+line)
    print(len(tokens))
    total=total+len(tokens)
f_out.write("\n"+"total: "+str(total))
print(total)
print(type(tokens))
f.close()
f_out.close()

with open('C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\funny.txt', 'r') as f:
    print(f.read())
print(f.closed)