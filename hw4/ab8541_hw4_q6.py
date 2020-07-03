def appearances(s,low,high):
    if low == high:
        return {s[low]:1}
    x = appearances(s, low+1, high)
    if s[low] in x:
        x[s[low]]+=1
    else:
        x[s[low]]=1

    return x

def main():
    i = appearances("Hello World", 0, 10)
    print(i)
main()
    
        
        
