def prime_number(number):
    if number <= 1:
        return False
    
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
            

number=int(input('Enter a number: '))
res=prime_number(number)
if res==True:
    print('Prime number')
else:
    print('Not a prime number')