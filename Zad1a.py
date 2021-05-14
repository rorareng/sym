import numpy as np

def fn(x):
    # This the equation to find the root
    return (x**3 - x - 1) #x**2 - x - 1

def find_root_interval():
    for x in range(0, 1000):
        if fn(x) < 0:
            lower_interval = x
            if fn(x+1) > 0:
                higher_interval = x + 1
                return lower_interval, higher_interval
    return False

def bisection():
    a,b = find_root_interval()
    print("Interval: [{},{}]".format(a,b))
    # Create a 1000 equally spaced values between interval
    mid = 0
    while True:
        prev_mid = mid
        mid = (a+b)/2
        print("Mid value: "+str(mid))
        # 0.0005 is set as the error range
        if abs(mid-prev_mid) < 0.0005:
            return mid
        elif fn(mid) > 0:
            b = mid
        else:
            a = mid

root = bisection()
print(root)