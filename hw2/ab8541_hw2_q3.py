def factors(num):
    initial = 1
    sqrt_num = num**.5
    l=[]
    while (initial<sqrt_num):
        if(num%initial==0):
            yield initial
            l.append(int(num/initial))
        initial +=1
    if(num%sqrt_num==0):
        yield int(sqrt_num)
    for i in range(len(l)-1, -1, -1):
        yield l[i]
    
        
        
def main():
    for curr_factor in factors(100):
        print(curr_factor, end = ' ')

main()
