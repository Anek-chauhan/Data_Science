def fib(nth_value):
    dict1=[0,1]
    if(nth_value== 1):
        print([0])
    if(nth_value>1):
        for i in range(1,nth_value-1):
            dict1.append(list(dict1)[-1]+list(dict1)[-2])
        print(dict1)    
nth_value=int(input("Enter nth value "))
fib(nth_value)          