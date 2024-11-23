class money:
    def __init__(self, r, p) -> None:
        self.r = r
        self.p = p
    def __iadd__(self, obj):
        a = self.r + obj.r
        b = self.p + obj.p
        c = money(a, b)
        return c
    
a = money(1, 2)
b = money(3, 4)
a += b
print(a.p, a.r)