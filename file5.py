# x = {'name':3,'age':20,'grades':[10,2,19]}

# for i in x:
#     if isinstance(x[i],list):
#         for j in range (len(x[i])):
#             print(x[i][j])

x = {'first':[1,2,3],'second':'me','third':50.2,'forth':0,'fifith':[4,5,5]}

# for i in x:
#     if isinstance(x[i],list):
#         x[i].append("insert")
#     elif isinstance(x[i],str):
#         x[i] = "you"
#     elif isinstance(x[i],float)or isinstance(x[i],int):
#         x[i] += 1

# check = 0

# for i in x:
#     if i == 'sixth':
#         check = 1

# if check == 0:
#     x['sixth'] = 10

# keys = list(x.keys())
# values = list(x.values())


# values_reversed = values[::-1]

# reordered_dict = {keys[i]: values_reversed[i] for i in range(len(keys))}


# print("original dict: \n", x)
# print("values after inversing: \n", reordered_dict)


print(f"\n{x}\n\nx after swap is :\n")

y=[]
for i in x:
    y.append(x[i])

list_lingth = len(y)

for i in range(list_lingth // 2):

    temp = y[i]
    y[i] = y[list_lingth - i - 1]
    y[list_lingth - i - 1] = temp

for i in range(len(y)):

    z=0
    for i in x:
        x[i]=y[z]
        z+=1

print(x,"\n")
