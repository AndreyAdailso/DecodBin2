""" Decodificador de binario para decimal"""


def bin_convert(bin_str):
    """ Recebe uma string representando um binario e retorna o valor em int decimal."""
    decimal = 0
    digt_bin = []

    for i in bin_str:
        digt_bin.append(int(i))
    
    for index in range(0, len(digt_bin)):
        n = digt_bin[index] * (2 ** (len(digt_bin) - 1 - index)) 
        decimal = decimal + n
        
    return decimal

def check_bin(bin_str):
    """Verifica se a string contem apenas 0 ou 1"""
    for i in bin_str:
        if i != '1' and i != '0':
            return False
    return True

#funções para a cifra de vienere 
def create_key(string, key):
    """Cria uma chave do tamanho da string para ser usada
    na função encryp_v e decryp_v."""
    len_string = len(string)
    len_key = len(key)
    
    key_extended = key * (len_string // len_key) + key[:(len_string % len_key)]

    return key_extended

def encryp_v(string, key):
    pass

def decryp_v(string, key):
    pass

#funções para sitema de numeração octal 

def check_octal(octal_str):
    validos = ['0', '2', '3', '4', '5', '6', '7']
    for index in octal_str:
        if index not in validos:
            return False
    return True
def octal_convet(octal_str):
    decimal = 0
    int_octal = []

    for i in octal_str:
        int_octal.append(int(i))
    
    for index in range(0, len(int_octal)):
        valor_algarismo = int_octal[index] * (8 ** (len(int_octal) - 1 - index))
        decimal = decimal + valor_algarismo

    return decimal


if __name__ == '__main__':
    input_user = input('Digite um numero em octal: ')
    if check_octal(input_user):
        print('Número valido!...')
        decimal = octal_convet(input_user)
        print(f'{input_user} = {decimal}')
    else:
        print('Número invalido!...')

    