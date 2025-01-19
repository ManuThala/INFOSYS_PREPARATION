def print_prime(inp1,inp2):
    for i in range(inp1,inp2+1):
        if check_prime(i):
            print(i,end=" ")



def check_prime(number):
    for i in range(2,int(number**0.5)+1):
        if  number % i == 0:
            return False
    return True
        
    

inp1=int(input('Enter first number: '))
inp2=int(input('Enter second number: '))
print_prime(inp1,inp2)
