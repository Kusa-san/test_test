# x = {'a':'a','b':'b','c':'c'}
# print(x)

# for i in x.values():
#     print(i)

# for i in x:
#     print(i)
# for i in x.values():
#    if i == 'c'
#     x[i]
#     y=x.get (i)
#     print(y)

# for i in x.values():
#     if i == 'c':
#         print(i)

dictionare = {'list':[1,2,3,10,12,14],'int':3,'float':11.0,'list2':[4,5,6]}

# for i in dictionare.values():
#     if type(i) == type(x):
#         print(i)

# for i in dictionare.values():
#     if isinstance(i,list):
#         for j in i:
#             print(j)
#         print(f"this is the end of the list {i}")

for i in dictionare:
    if isinstance(dictionare[i],list):
        for j in range (len(dictionare[i])):
            dictionare[i][j]+=1
        print(dictionare)
        