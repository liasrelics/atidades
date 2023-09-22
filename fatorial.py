def fatorial (i:int):
    if (i == 1):return 1
    else:
        return i * fatorial (i - 1)
print (fatorial(7))