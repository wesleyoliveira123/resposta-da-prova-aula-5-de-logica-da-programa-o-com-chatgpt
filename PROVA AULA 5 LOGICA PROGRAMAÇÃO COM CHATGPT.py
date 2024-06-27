print("---------------SALA DE AULA---------")
print()
numero=int(input("digite o número de alunos: "))
print("---------------------------------------")
soma_medias=0
for i in range(numero):
    i+=1
    print(f"aluno de numero {i}! ")
    nome=input("digite o nome do aluno: ")
    nota1=float(input("digite a primeira nota do aluno: "))
    nota2=float(input("digite a segunda nota do aluno: "))
    nota3=float(input("digite a terceira nota do aluno: "))

    media=(nota1+nota2+nota3)/3
    soma_medias+=media

    if (media>=7):
        print(f"a media do aluno de numero {i}, que se chama {nome}, foi de {media}, parabens,APROVADO!")
    else:
        print(f"a media do aluno de numero {i}, que se chama {nome}, foi de {media}, desculpe,REPROVADO!")
    print("---------------------------------------")
    media_geral=soma_medias/numero
print(f"a media geral da turma foi {media_geral}")