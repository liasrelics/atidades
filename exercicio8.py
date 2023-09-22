import math
gravidade = 9.8

a = float(input("Digite a coordenada X do canhão: "))
b = float(input("Digite a coordenada Y do canhão: "))
forca = float(input("digite a força inicial:"))
forca_horizontal = float(input("Digite a força horizontal em Newtons: "))
forca_vertical = float(input("Digite a força vertical em Newtons: "))
angulo = float(input("Digite o ângulo em graus: "))

def v_inicial(forca, massa):
    v0 = forca/massa
    return v0

def v_inicialHorizontal(forca, massa, angulo):
    v0 = v_inicial(forca, massa)
    v0x = v0 * math.cos(math.radians(angulo))
    return v0x

def v_inicialVertical(forca, massa, angulo):
    v0 = v_inicial(forca, massa)
    v0y = v0 * math.sin(math.radians(angulo))
    return v0y

def v_horizontal(forca, massa, angulo, tempo):
    if(tempo >= t_voo(forca, massa, angulo)): return 0
    v0x = v_inicialHorizontal(forca, massa, angulo)
    vx = v0x
    return v0x

def v_vertical(forca, massa, angulo, tempo):
    if(tempo >= t_voo(forca, massa, angulo)): 
        v0y = v_inicialVertical(forca, massa, angulo)
    vy = v0y - (gravidade * tempo)
    return vy

def t_voo(forca, massa, angulo):
    v0y = v_inicialVertical(forca, massa, angulo)
    t_max = 2 * v0y / gravidade
    return t_max

def alcance(forca, massa, angulo):
    t_max = t_voo(forca, massa, angulo)
    v0x = v_inicialHorizontal(forca, massa, angulo)
    x_max =  v0x * t_max 
    return x_max

print(f"Velocidade inicial do lançamento oblíquo: {v_inicial} m/s")
print(f"Tempo total de voo: {t_voo} segundos")
print(f"Velocidade vertical: {v_vertical} m/s")
print(f"Velocidade horizontal: {v_horizontal} m/s")
