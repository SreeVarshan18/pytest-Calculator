def add2no(x, y):
    return x+y

def sub2no(x ,y):
    return x-y

def mul2no(x ,y):
    return x*y

def div2no(x ,y):
    return x/y

if __name__ == "__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    sum = add2no(a, b)
    diff = sub2no(a, b)
    prod = mul2no(a, b)
    div = div2no(a, b)

    print(sum)
    print(diff)
    print(prod)
    print(div)