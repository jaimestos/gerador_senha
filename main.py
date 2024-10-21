import random as rd
import string as st

def gerar_senha (tamanho=12):
    numeros = True
    caracteres_especiais = True
    caracteres = st.ascii_letters
    if numeros:
        caracteres += st.digits
    if caracteres_especiais:
        caracteres_especiais_aceitos = "!@#$%&*"
        caracteres += caracteres_especiais_aceitos
    senha = ''.join(rd.choice(caracteres) for i in range(tamanho))
    return senha

teste = gerar_senha(20) 
print(teste)