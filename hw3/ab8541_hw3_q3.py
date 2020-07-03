def find_duplicates(lst):
    lst_new = [0]*len(lst)
    #print(lst_new)
    #print(lst_new)
    fin_lst = []
    for x in (lst):
        #print(x)
        lst_new[x] += 1
        
    #print(lst_new)
    
    for x in range(len(lst_new)):
        if lst_new[x]>1:
            fin_lst.append(x)
    return fin_lst

def main():
    y = find_duplicates([2,4,4,1,2])
    print(y)
main()
    
        
