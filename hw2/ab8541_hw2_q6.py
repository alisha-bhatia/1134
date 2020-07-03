def two_sum(srt_lst, target):
    answer = None
    left,right = 0,len(srt_lst)-1

    while left<right:
        if (srt_lst[right] + srt_lst[left] >target):
             right = right -1
        elif (srt_lst[left] + srt_lst[right] <target):
            left = left+1
        elif srt_lst[right] + srt_lst[left] ==target:
            return (left, right)
            
    return ()
        

def main():
    y = two_sum([-2,7,11,15,20,21], 22)
    print(y)
main()
            
            
            
            
            
