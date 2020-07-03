def flat_list(nested_lst, low, high):
    ans = []
    for i in range(low, high+1):
        if  type(nested_lst[i]) == list:
            ans.extend(flat_list(nested_lst[i], 0, len(nested_lst[i])-1))
        else:
            ans.append(nested_lst[i])
            
    print(ans)
    return ans
        
def main():
    i = flat_list([[1,2], 3, [4, [5, 6, [7], 8]]], 0,2)
    print(i)
main()
        
