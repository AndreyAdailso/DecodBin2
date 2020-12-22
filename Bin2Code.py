""" Decodificador de binario para decimal"""


def bin_convert(bin_str):
    """ Recebe uma string representando um binario e retorna o valor em int decimal."""
    decimal = 0
    cont = 0 
    digt_bin = []

    for i in bin_str:
        digt_bin.append(int(i))
    
    for index in range(len(digt_bin)-1, -1, -1):
        n = digt_bin[index] * (2**cont)
        decimal = decimal + n
        cont = cont + 1
        
    return decimal
    
while True:     
    print("Digite o binario que deseja converter.")
    print(">>>", end='')
    input_bin = str(input())
    
    deci_bin = bin_convert(input_bin)

    print(input_bin,"=", deci_bin)
    print("FIM")
    break


