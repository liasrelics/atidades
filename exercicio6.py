minhalista = ['coca ou pepsi?',
              'doce ou salgado?',
              'pizza ou hambúrguer?',
              'samsung ou motorola?',
              'treloso ou futurinhos?',
              'morrer ou perder a vida?']

respostasdalista = ['coca',
                    'salgado',
                    'pizza',
                    'motorola',
                    'treloso',
                    'morrer']

nota = 0

for i in range(len(minhalista)):
   respostas = input(minhalista[i])
   if(respostas == respostasdalista[i]):
      print("acertou, mt que bem")
      nota = nota + 1
   else:
      print("burro")

print(f"sua nota foi... {nota} ")