print("For Square:type any number to get square root")
s = lambda x:x*x
print("Square root is :",s(x=int(input())))

name_length = map(len,['Ishani','Jain','Rehaana','Dev','Anny'])
print(name_length)

# total = reduce(lambda a,x:a+x,[0,1,2,3,4])
# print(total)
arr = [1,2,3,4,5,6]
s = [i for i in filter(lambda x:x<4,arr)]
print(s)