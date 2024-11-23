a = 10
def hi(a):
    if a == 0:
        print(a)
        print("avlo dan")
        return
    return hi(a-5) or hi(a-1)
hi(a)
