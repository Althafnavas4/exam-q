# l=[1,2,3,3,2,1]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#-----------------------------------------------------

a=65
for i in range(1,5):
    for j in range(i):
        print(chr(a-j),end=' ')
    print(' ')
    a+=1