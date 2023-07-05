
def le_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo_texto = arquivo.read()
    return conteudo_texto

def conta_caracteres(conteudo_texto):
    contador_caracteres={}
    for caractere in conteudo_texto:
        if caractere in contador_caracteres:
            contador_caracteres[caractere] += 1
        else:
            contador_caracteres[caractere] = 1
    return contador_caracteres

nome_arquivo = './poesias-margareth-freire/curvas-e-retas.txt'
contagem = conta_caracteres(le_arquivo(nome_arquivo))
print(len(contagem))
print(contagem)