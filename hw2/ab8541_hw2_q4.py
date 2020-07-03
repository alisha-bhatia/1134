def e_approx(n):
    e_approx = 0
    d = 1
    for x in range (1, n+2):
        e_approx+=(1/d)
        d*=x
    return e_approx

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
main()
