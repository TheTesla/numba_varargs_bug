
def f0(*args):
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

def f1(*args, x):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

def f2(*args, x=8.8):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

def f3(x, *args):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

def f4(x=8.8, *args):
    print("  x =", x)
    for i, a in enumerate(args):
        print("  args[", i, "] =", a)

def f():
    print("")
    print("expected results")
    print("f0(1.1,2.2,3.3,4.4,5.5,6.6):")
    f0(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f1(1.1,2.2,3.3,4.4,5.5,6.6):")
    try:
        f1(1.1,2.2,3.3,4.4,5.5,6.6)
    except Exception as e:
        print(e)
    print("f1(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    f1(1.1,2.2,3.3,4.4,5.5,x=6.6)
    print("f2(1.1,2.2,3.3,4.4,5.5,6.6):")
    f2(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f2(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    f2(1.1,2.2,3.3,4.4,5.5,x=6.6)
    print("f3(1.1,2.2,3.3,4.4,5.5,6.6):")
    f3(1.1,2.2,3.3,4.4,5.5,6.6)
    print("f3(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    #f3(1.1,2.2,3.3,4.4,5.5,x=6.6)
    #print("f4(1.1,2.2,3.3,4.4,5.5,6.6):")
    f4(1.1,2.2,3.3,4.4,5.5,6.6)
    #print("f4(1.1,2.2,3.3,4.4,5.5,x=6.6):")
    #f4(1.1,2.2,3.3,4.4,5.5,x=6.6)

f()

