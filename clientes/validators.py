import re
from validate_docbr import CPF


def validate_cpf(cpf):
    cpf = CPF()
    return cpf.validate(cpf)
        
def validate_rg(rg):
    return len(rg)!= 9

def validate_nome( nome):
        return not nome.isalpha()
    
def validate_celular(celular):
    ''' modelo 81 99999-9999'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
