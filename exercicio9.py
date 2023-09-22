# Alunas: Geovanna Leticia e Júlia Vitória

# Escreva um programa em python que

# * Receba um número inteiro e faça uma contagem regressiva
# * Receba um número inteiro e calcule a soma recursiva ate 1
# * Receba uma string e retorne a string invertida

# DICA: USE Import time e Time.sleep(1) / para esperar um segundo.

#A) CONTAGEM REGRESSIVA

import time 

# * DEF: definição de uma função
# * FOR I IN RANGE: loop q percorre uma sequencia de numeros num intervalo de tempo 

#A) CONTAGEM REGRESSIVA

#DEF: definição de uma função
#FOR I IN RANGE: loop q percorre uma sequencia de numeros num intervalo de tempo 

def contagem_regressiva(número):
    for i in range(número, 0, -1):  #o número é o ponto de partida, o 0 é o ponto final, já o -1 é a subtração de cada i 
        print(i)
        time.sleep(1)  #espera 1 segundo p contagem regressiva
    print("acabou a contagem, bb")

print("contagem regressiva de 10: ")
contagem_regressiva(10)

# ? //////////////////////////////////////////////////////////////////////////
#B) SOMA RECURSIVA ATÉ 1

#IF: executa o código apenas e a condição for true
#ELSE: executa o código quando a condição IF não for verdadeira
#RETURN: usada nas funções p especificar o valor da função que deve retornar

def soma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + soma_recursiva(numero - 1)

numero = int(input("Digite um número, pelo amor de god usopp: "))
resultado = soma_recursiva(numero)
print(f"ei, boy, a soma de tudin aí ate 1 foi: {resultado}")

#? ///////////////////////////////////////////////////////////////////////////

#C) SOMA DE POTENCIA

def potencia(base, expoente):
    if expoente == 0: return 1
    else: return base * potencia(base, expoente - 1)

print(f" 2 elevado a 2: {potencia(2, 2)}") 
print(f" 2 elevado a 3: {potencia(2, 2)}") 
print(f" 3 elevado a 2: {potencia(2, 2)}") 
print(f" 3 elevado a 3: {potencia(2, 2)}") 


# ? //////////////////////////////////////////////////////////////////////////

#D) STRING INVERTIDA // isso aq me endoidou

def string_invertida1(texto): #texto pq é string
   return texto[:: -1] #expressão de fatiamento p inveter string 

#o primeiro ponto indica que não foi especificado um ponto inicial, emt começara pela primeira letra
#o segundo ponto indica que não especificou um ponto final, ent vai ate a ultima letra
#e o valor - 1 significa que os elementos foram pegados de tras p frente
#os dois pontos são usados p "fatiar"

string_sem_ser_invertida = (input("Digite uma palavrinha pra ver a magicaaa: "))
string_invertida2 = string_invertida1(string_sem_ser_invertida)
print(f"DEUAAAAA, VE QUE BAZI ESSA MAGICAA: {string_invertida2}")