def remove_all(lst, value):
    ind = 0
    for x in range(len(lst)):
        if lst[x]!= value:
            lst[ind] = lst[x]
            ind+=1
    del lst[ind:]
    return lst

def main():
    i = remove_all([1,2,3,3,4,5,3],3)
    print(i)
main()
