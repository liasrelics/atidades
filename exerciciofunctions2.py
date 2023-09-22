
import math

x = float(input("Digite a coordenada x do canhão: "))
y = float(input("Digite a coordenada y do canhão: "))
forca_horizontal = float(input("Digite a força horizontal em newtons: "))
forca_vertical = float(input("Digite a força vertical em newtons: "))
angulo = float(input("Digite o ângulo em graus: "))

velocidade_inicial = math.sqrt(forca_horizontal * 2 + forca_vertical * 2) / 5

tempo_voo = (2 * velocidade_inicial * math.sin(angulo)) / 9.8

queda_x = x + velocidade_inicial * math.cos(angulo) * tempo_voo
queda_y = y + (velocidade_inicial * math.sin(angulo) * tempo_voo) - (0.5 * 9.8 * tempo_voo ** 2)

velocidade_vertical = velocidade_inicial * math.sin(angulo) - (9.8 * tempo_voo)
velocidade_horizontal = velocidade_inicial * math.cos(angulo)

distancia_horizontal = queda_x - x

print(f"Velocidade inicial do lançamento oblíquo: {velocidade_inicial} m/s")
print(f"Tempo total de voo: {tempo_voo} segundos")
print(f"Local de queda do projétil: ({queda_x}, {queda_y})")
print(f"Velocidade vertical: {velocidade_vertical} m/s")
print(f"Velocidade horizontal: {velocidade_horizontal} m/s")
print(f"Distância horizontal entre o ponto de lançamento e o local da queda: {distancia_horizontal} metros")


#geovanna leticia e julia vitoria