# list
# l=[1,2,3,3,2,1]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#-----------------------------------------------------

# pattern 
# a=65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(a-j),end=' ')
#     print(' ')
#     a+=1
#--------------------------------------------------------

# factorial

# def fun(value):
#     fact=1
#     for i in range(1,value+1):
#         fact=fact*i
#     return fact
# print(fun(5))
# print(fun(6))
#------------------------------------------------------------


#-------------------------------------------------------

# d={1:'one',2:'two'}
# d1={}
# for i in d:
#     d1[d[i]]=i
# print(d1)

#-----------------------------------------------------------

f=open('demo.txt','r')
l=f.readlines()
f.seek(0)
long=''
for i in range(len(l)):
    b=f.readline().strip()
    c=b.split(' ')
    for j in c:
        if j!='' and len (j)>len(long):
            long=(j)
print(long)