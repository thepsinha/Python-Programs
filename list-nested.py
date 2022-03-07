if __name__ == '__main__':
    l1=[]
    for _ in range(int(input("Enter range."))):
       name = input("Name :  \n")
       score = float(input("Score :  "))
       l1.append([name,score])
    l1.sort(key=lambda x:(x[1],x[0]))
    n = [i[0] for i in l1]
    s = [i[1] for i in l1] 
    min_val = min(s)
    while s[0] == min_val:
        s.remove(s[0])
        n.remove(n[0])
    for x in range(0,len(s)):
        if s[x] == min(s):
             print(n[x])

