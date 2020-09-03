def fibonacci(n=100000):
    result= []
    a, b = 0, 1
    while a < n:
        
        a, b = b, a+b
        if (a) % 2 == 0:
            result.append( a )
            continue
            
          
    return result 

print(" The sum of even fibonacci numbers less than 100,000 is:  " + str(sum(fibonacci())))