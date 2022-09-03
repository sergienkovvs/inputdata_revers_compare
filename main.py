inputdata = ["страна","шалаш","летел","вертолёт","учу","мэм","язык"]

revers = inputdata[::-1]
compare = revers == inputdata

def reversed_wars(a):
    return a[::-1] == a

res = list(filter(reversed_wars, inputdata))
print(res)