


prime_num = []    
for num in range(2,100001):
    
    if num > 1:
        for i in range (2, num):
            if(num % i) == 0:
                break
        else:           
             prime_num.append(num)               

print("The sum of prime numbers less than 100,000 is:  " + str(sum(prime_num)))
import statistics
print("The median of prime numbers less than 100,000 is: " + str(statistics.median(prime_num)))

            
    
    

    