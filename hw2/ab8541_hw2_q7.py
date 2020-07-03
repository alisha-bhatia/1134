def findChange(lst01):
    mid = len(lst01)-1//2
    left,right = mid-1,mid+1
    ans_found = False
    index =0
    
    while left<=right and ans_found != True:
        if lst01[left] == 0 and lst01[right]==1:
            ind = right
            return right
            ans_found = True
        elif (lst01[right]==0 and lst01[left]==0):
            mid = mid+1
            
            
            
    return None
        

def main():
    y=findChange([0, 0, 0, 0, 0, 1, 1, 1])
    print(y)
main()
    
