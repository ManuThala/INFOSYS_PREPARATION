def smallest_element(array):
    for i in range(len(array)):
        if array[i]<array[0]:
            array[0]=array[i]
    return array[0]
    
def largest_element(array):
    if array==0:
        return False
    for i in range(len(array)):
        if array[i]>array[0]:
            array[0]=array[i]
    return array[0]

array=[2,3,4,65,7,9,8]
res=smallest_element(array);
res1=largest_element(array);
print(res)
print(res1)