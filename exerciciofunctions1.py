# implemente o programa em pyton,
# que receba dois valores e retorne
# a media entre eles, e defina uma função
# customizada para média

def media (a, b):
    s = a + b 
    m = s / 2
    return m

a = float(input("digite a primeira media: "))
b = float(input("digite a segunda media: "))

print(f"A media de {a} e {b} é: {media(a,b):.2f} ")
