MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

#1 FORMA
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
    
#2 FORMA
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


#3 FORMA
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode adiantar aulas teóricas apenas.")
else:
    print("Ainda não pode tirar a CNH.")
    
#UTILIZANDO TERNARIOS
status = "Maior de idade, pode tirar a CNH." if idade >= MAIOR_IDADE else "Não pode tirar CNH."

print(status)