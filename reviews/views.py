from django.shortcuts import render

def index(request):
    """
    FUNÇÃO INICIAL PARA A VIEW DE REVIEWS
    """

    name = "Sol"
    
    return render(request, "base.html", {"name" : name})

def pesquisa_livro(resquest):
    '''
    FUNÇÃO PARA REALIZAR A BUSCA DE LIVROS POR UM TERMO PASSADO PELO USUÁRIO\n
    O contexto busca pela chave `termo_busca` e a envia pra o contexto.
    '''

    termo_busca = resquest.GET.get("termo_busca") or "termo não informado :/"

    return render(resquest, "resultado_pesquisa.html", {"termo_busca" : termo_busca})
    
