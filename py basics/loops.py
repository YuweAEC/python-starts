# write loops program on python to understand the concept of loops in python 
import sys

print(sys.argv)

x=int(sys.argv[1])
y=int(sys.argv[2])

for i in range(x,y):
    print(i)
while x<y:
    print(x)
    x+=1

