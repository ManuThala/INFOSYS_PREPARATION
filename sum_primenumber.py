def prime_number(num):
    if num<=1:
        return False;
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False;
    return True;

def sum_prime(num1,num2):
    sum=0;
    for i in range(num1,num2):
        if prime_number(i):
            sum+=i;
    return sum;


num1=int(input('Enter first number:'));
num2=int(input('Enter Second number:'));
res=sum_prime(num1,num2);
print(f'Sum of {num1} and { num2} is {res}');
