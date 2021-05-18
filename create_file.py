f = open("test.txt",'w')

for i in range(1,11):
    data  = "test %d\n" %i
    f.write(data)


f.close