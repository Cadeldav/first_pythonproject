while True:
    print("\n1-18 a 28")
    print("2-IRS,SEGURANCA SOCIAL, HORAS")
    print("3-INTERMEDIO")
    print("0-EXIT")

    option =  int(input("Escolha uma opção: "))

    match option:

        case 1:
            soma_total = 0
            soma_intervalo = 0
            cont_intervalo = 0

            for i in range(7):
                temp = float(input(f"Digite a temperatura {i + 1}: "))

                # Soma total
                soma_total += temp

                # Soma apenas das temperaturas entre 18 e 28 (inclusive)
                if 18 <= temp <= 28:
                    soma_intervalo += temp
                    cont_intervalo += 1

            # Cálculo das médias
            media_total = soma_total / 7

            if cont_intervalo > 0:
                media_intervalo = soma_intervalo / cont_intervalo
            else:
                media_intervalo = 0  # ou "Nenhum valor no intervalo"

            print(f"Média de todas as temperaturas: {media_total:.2f}")
            print(f"Média das temperaturas entre 18 e 28 graus: {media_intervalo:.2f}")

        case 2:

                # Ler dados de entrada
            num_empregado = input("Digite o número do empregado: ")
            horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
            valor_hora = float(input("Digite o valor por hora (€): "))

            # Calcular salário bruto (considerando horas extra)
            if horas_trabalhadas <= 35:
                # Só horas normais
                salario_bruto = horas_trabalhadas * valor_hora
            else:
                # 35 horas normais + restantes como extra
                horas_normais = 35
                horas_extra = horas_trabalhadas - 35

                salario_normais = horas_normais * valor_hora
                salario_extras = horas_extra * valor_hora * 1.5  # cada hora extra vale 1.5x

                salario_bruto = salario_normais + salario_extras

                # Determinar a taxa de IRS
            if salario_bruto >= 1000:
                taxa_irs = 0.20
            elif salario_bruto >= 600:
                taxa_irs = 0.15
            else:
                taxa_irs = 0.10

                # Calcular os descontos
            valor_irs = salario_bruto * taxa_irs
            seguranca_social = salario_bruto * 0.11

            # Calcular salário líquido
            salario_liquido = salario_bruto - valor_irs - seguranca_social

            # Mostrar resultados
            print("\n--- Recibo de Vencimento ---")
            print(f"Número do empregado: {num_empregado}")
            print(f"Salário bruto: {salario_bruto:.2f} €")
            print(f"IRS ({taxa_irs * 100:.0f}%): {valor_irs:.2f} €")
            print(f"Segurança Social (11%): {seguranca_social:.2f} €")
            print(f"Salário líquido: {salario_liquido:.2f} €")

        case 3:
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            n3 = int(input("Digite o terceiro número: "))

            if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
                print(f"O intermedio é {n1}")
            elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3 ):
                print(f"O intrmedio é {n2}")
            else:
                print(f"O intermedio é {n3}")

        case 0:
            print("EXIT...")
            break
        case _:
            print("invalid option3")
