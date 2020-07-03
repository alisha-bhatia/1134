def func(num):
    counter = 0
    a = 1
    b = 1
    while counter < num: 
        yield a 
        a, b = b,a + b
        counter += 1

def main():
    for i in func(8):
        print(i, end = " ")
        
main()
