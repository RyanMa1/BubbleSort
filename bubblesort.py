def bubblesort(l):
    for x in range(len(l)):
        if x == len(l)-1:
            basecase = l[len(l)-1]
            return basecase, l
        elif l[x] < l[x+1]:
            continue
        elif l[x] > l[x+1]:
            l[x], l[x+1] = l[x+1], l[x]
        else:
            continue
def recursion(l):
    basecase, l = bubblesort(l)
    if len(l) == 1:
        return l
    for x in l:
        if x > basecase:
            return recursion(l[:-1]) + l[-1:]
        elif x < basecase:
            continue
        else:
            return recursion(l[:-1]) + l[-1:]
def main():
    l = [7,6,1,2,1,3,3,2]
    print(recursion(l))
main()
