# 'r+' read then write method
f  = open('s.txt','r+')
print(f.tell())
d = f.read()
print(f.tell())
f.write("lucky")
print(f.tell())
print(d)