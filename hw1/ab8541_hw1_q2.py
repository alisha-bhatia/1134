def shift(lst, k, direction = None):
    if direction == "right":
        for x in range(0,k):
            lst.insert(0,lst.pop())
    else:
        for x in range(0,k):
            lst.append(lst.pop(0))
    return lst

def main():
   y = shift([1,2,3,4,5,6],2)
   print(y)
main()
