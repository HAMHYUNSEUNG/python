
# write 함수 테스트 
f = open("test.txt", 'w')

for i in range(1,11):
    data  = "test %d\n" %i
    f.write(data)

# read 함수 테스트 
f = open("test.txt", 'r')
data = f.read()
print(data)

f.close