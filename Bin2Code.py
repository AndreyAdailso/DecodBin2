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

def check(bin_str):
    """Verifica se a string contem apenas 0 ou 1"""
    for i in bin_str:
        if i != '1' and i != '0':
            return False
    return True

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

if __name__ == '__main__':
    mens = input("mesaguem: ")
    cha = input("chave: ")
    print(create_key(mens, cha))
    
    while False:     
        print("Digite o binario que deseja converter.")
        print(">>>", end='')
    
        input_bin = str(input())
    
        if check(input_bin) == True:
            deci_bin = bin_convert(input_bin)
            print(input_bin,"=", deci_bin)
            break
        else:
            print("Erro: Por favor Digite um número binario valido.")
