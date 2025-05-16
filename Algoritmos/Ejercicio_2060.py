casos=int(input())
lista_numeros=input().split(" ")

mlt_2=0
mlt_3=0
mlt_4=0
mlt_5=0

for i in range (casos):
    if(int(lista_numeros[i])%2==0):
        mlt_2=mlt_2+1
    if(int(lista_numeros[i])%3==0):
        mlt_3=mlt_3+1
    if(int(lista_numeros[i])%4==0):
        mlt_4=mlt_4+1
    if(int(lista_numeros[i])%5==0):
        mlt_5=mlt_5+1
print(f"{mlt_2} Multiplo(s) de 2")
print(f"{mlt_3} Multiplo(s) de 3")
print(f"{mlt_4} Multiplo(s) de 4")
print(f"{mlt_5} Multiplo(s) de 5")