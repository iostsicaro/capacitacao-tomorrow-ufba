def converter_comprimeiro(valor_converter, medida_entrada, medida_saida):
    unidades = {
        'cm': 1,
        'm': 100,
        'km': 100000,
        'polegada': 2.54,
        'pe': 30.48,
        'jarda': 91.44,
        'milha': 160934
    }

    for x, y in unidades.items():
        if x == medida_saida:
            valor_auxiliar = valor_converter * unidades[medida_entrada]
            valor_convertido = valor_auxiliar / y
            
            print('A conversão de ' + str(valor_converter) + ' ' + medida_entrada + ' = ' + str(valor_convertido) + ' ' + medida_saida)
            break

valor = float(input("Digite o valor a ser convertido: "))
unidade_de_entrada = input("Digite a unidade de entrada: ")
unidade_de_saida = input("Digite a entrada de saida: ")

converter_comprimeiro(valor, unidade_de_entrada, unidade_de_saida)