while True:
    print("\n1 - grade 0-20")
    print("2 - decrement")
    print("3 - increment ")
    print("4 - fahrenheit to celsius ")
    print("0 - exit")

    option = int(input("Escolha uma opção: "))

    match option:
        case 1:
           grade = int(input("input your grade"))
           if 0<= grade <=20:
                print ("your grade its valid.")
           else:
                 print (f"your grade {grade} its invalid, must be between 0 and 20!")
        case 2:
            number = int(input("input a positive number:"))
            if number <=0:
                print ("Your number must be positive!")
            else:
                 while number >= 0:
                    print(number)
                    number = number -1
        case 3:
            sum = 0
            digits= 0

            while True:
                number = int(input("Digite um valor inteiro (<= 0 para terminar): "))

                if number <= 0:
                    break

                sum += number
                digits += 1

                print("the total of the sum is:", sum)
                print("de total of digits:", digits)
        case 4:
             for celsius in range(10, 21):  # 21 porque o 'stop' não é incluído
                fahrenheit = (celsius * 9 / 5) + 32
                print(f"{celsius}°C = {fahrenheit}°F")

        case 0:
            print("exit...")
            break
        case _:
            print("invalid option")
