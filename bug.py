from numba import njit

@njit
def f0(*args):
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

@njit
def f1(*args, x):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

@njit
def f2(*args, x=8.8):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

@njit
def f3(x, *args):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

@njit
def f4(x=8.8, *args):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

@njit
def f():
    print("f0(1.1,2.2,3.3,4.4,5.5,6.6):")
    f0(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f1(1.1,2.2,3.3,4.4,5.5,6.6):")
    f1(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f1(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    f1(1.1,2.2,3.3,4.4,5.5,x=6.6)
    print("f2(1.1,2.2,3.3,4.4,5.5,6.6):")
    f2(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f2(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    f2(1.1,2.2,3.3,4.4,5.5,x=6.6)
    print("f3(1.1,2.2,3.3,4.4,5.5,6.6):")
    f3(1.1,2.2,3.3,4.4,5.5,6.6)
    #print("f3(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    #f3(1.1,2.2,3.3,4.4,5.5,x=6.6)
    print("f4(1.1,2.2,3.3,4.4,5.5,6.6):")
    f4(1.1,2.2,3.3,4.4,5.5,6.6)
    #print("f4(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    #f4(1.1,2.2,3.3,4.4,5.5,x=6.6)

f()

