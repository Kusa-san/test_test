# x=1
# while x<=20:
#     print(x)
#     x+=3
# x = [1,2,3]
# print(x)
# x[2]= "kusa"
# print(x)
# x += [1]
# print(x)
# x2=x.pop(2)
# print(x2)
# x.append("kusa")
# print(x)
# x.insert(1, "Mohamed")
# print(x)
# for i in x:
#     print(i)

# li = [1,2,3,4,5]
# for i in range (5):
#     li[i]+=1
# print(li)

# li=[2,4,6]
# i=0
# while i<6:
#     li.insert((i+1),1)
#     i+=2
# print(li)

# li = [1,'s',3,"mohamed"]

# print(f"the list length is {len(li)}")

# for i in range(len(li)):
#     print(li[i])

# a=0
# li = [1,2,3,4,5]
# for i in range(len(li)):
#     a = a + li[i]
# print(f"the summ of the list is {a}")

a = 0.0
li = [1.0, 'abc', 2.5, 'b', 3, 'c', 4.11, 'd', 5, 'e']

for i in range(len(li)):
    if isinstance(li[i], (int, float)):
        a = a + li[i]
        print(f"The sum of the list so far is {a}")
    if isinstance(li[i], str):
        print(f"The value of the element in the list is {li[i]}")