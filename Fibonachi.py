def fibonacci(n):
    dict1=[0,1]
    if(n== 1):
        print([0])
    if(n>1):
        for i in range(1,n):
            dict1.append(list(dict1)[-1]+list(dict1)[-2])
        return  dict1
n = int(input())
print(fibonacci(n))    