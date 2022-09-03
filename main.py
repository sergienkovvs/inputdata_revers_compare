inputdata = ["Страна","шалаш","Летел","вертолёт","УЧУ","мэм","язык"]

def reversed_wars(a):
    a = a.lower()
    return a[::-1] == a

res = list(filter(reversed_wars, inputdata))
print(res)