def wepondam(x):
    return x

def naturaldam(str):
    return int(str/3)

def hit(w, n):
    def damage(x):
        return w(x) + n(x)
    return damage

result = hit(wepondam, naturaldam)
print(result(6))