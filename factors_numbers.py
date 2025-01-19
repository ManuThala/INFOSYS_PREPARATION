def factors(number):
    factors=[]
    for i in range (1,number+1):
        if number % i ==0:
            factors.append(i)
    return factors
            
  
number=int(input('Enter a number: '));
res=factors(number)
print(res)