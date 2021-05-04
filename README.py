# Criador-de-arvore-binaria-de-busca
cria árvore binaria, tem função de mostrar a árvore e ainda calcula a altura.
class Arvore_binaria:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
def inserir(raiz,dado):
    if not raiz:
        return Arvore_binaria(dado)
    else:
        if raiz.dado == dado:
            return raiz
        elif dado < raiz.dado:
            raiz.esq = inserir(raiz.esq, dado)
        else:
            raiz.dir = inserir(raiz.dir, dado)
    
    
    return raiz
