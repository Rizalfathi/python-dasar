def new_func1():
    a = [1, 2, 3, 4, 5]
    b = a[1:4]

    print(b)

    def new_func(a):
        c = a[:3]
        print(c)

        d = a[3:]
        print(d)

    new_func(a)

new_func1()