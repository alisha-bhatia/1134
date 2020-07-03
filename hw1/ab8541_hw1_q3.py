#3a:
def squares_sum(n):
    total = 0
    for x in range(1,n+1):
        total = total+ x**2
    return total
#3b
sum(k*k for k in range(3))

#3c
def odd_squares_sum(n):
    total = 0
    for y in range(1,n+1):
        if (y%2==1):
            total = total+y
    return total

def main():
    y = squares_sum(3)
    print(y)
main()

#3d
sum(k*k for k in range(4) if (k%2 == 1))
