dict1=[0,1]
def fib(nth_value):
    if(nth_value== 0):
        print([0])
    else:
        for i in range(1,nth_value-1):
            dict1.append(list(dict1)[-1]+list(dict1)[-2])
        print(dict1)    
nth_value=int(input("Enter nth value "))
fib(nth_value)          
