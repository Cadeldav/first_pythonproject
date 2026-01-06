while True:
    print("\n1 -range 0-20")
    print("2 - IMC")
    print("3 - volume da esfera ")
    print("4 - função raio da esfera ")
    print("5 - listas ")
    print("0 - exit")

    option = int(input("Escolha uma opção: "))

    match option:
        case 1:
            soma=0
            i=20

            for i in range (20 ,-1, -2):
                soma=soma+i
            print(soma)

        case 2:
            massa = float(input("Digite o seu peso em kilos:"))
            altura = float(input("Digite o sua altura:"))

            imc = massa/(altura+altura)
            print(f"O seu imc é ", round(imc,2))

        case 3:
            import math

            raio = float(input("Digite o raio da esfera em cm: "))

            volume = (4 / 3) * math.pi * (raio ** 3)

            print("O volume da esfera é:", volume)

        case 4:
            import math


            def calcular_volume(raio):
                volume = (4 / 3) * math.pi * (raio ** 3)
                return volume


            raio = float(input("Digite o raio da esfera em cm: "))

            resultado = calcular_volume(raio)

            print("O volume da esfera é:", resultado)

        case 5 :
            lista1 = ['Iva', 25, 'Rui', 19, 'Rato', 'abc', 33]

            print(lista1)  # a)
            print(lista1[2:5])  # b)
            print(lista1[:3])  # c)
            print(lista1[3:])  # d)

            lista2 = ['Python', 2024]
            nova_lista = lista1 + lista2

            print(nova_lista)  # e)


        case 0:
            print("exit...")
            break

        case _:
            print("invalid option")





