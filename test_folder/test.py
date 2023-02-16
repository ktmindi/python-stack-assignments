def manyargs(arg1, *args):
        for a in args:
            print(a)

manyargs("one","two","three")