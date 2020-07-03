def split_parity(lst):
    right = 1
    left = 0
    while right <= (len(lst)-1):
        if((lst[left] + lst[right])%2 !=0):
            if (lst[left]%2 == 0):
                lst[right], lst[left],= lst[left],lst[right]
            left = left +1
            right+=1
        elif (lst[left]%2==0):
            right+=1
        else:
            left = left +1
            right+=1
    return lst


def main():
    y=split_parity([1,2,3,4])
    print(y)
main()
    
