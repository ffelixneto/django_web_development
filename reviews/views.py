from django.shortcuts import render
from django.http import HttpResponse


from .models import Book, Review
from .utils import average_rating

### FUNÇÕES INICIAIS

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
    
def welcome_view(request):
    '''
    FUNÇÃO PARA EXIBIÇÃO DE BOAS VINDAS
    '''

    return render(request, 'base.html')


### FUNÇÕES LISTAGEM COM TEMPLATE PARA LIVROS 

def book_list(request):
    """
    FUNÇÃO PARA LISTAR OS LIVROS
    """

    books = Book.objects.all()
    book_list = []

    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        
        else:
            book_rating = None
            number_of_reviews = 0
        
        book_list.append(
            {
                'book' : book, 
                'book_rating' : book_rating,
                'number_of_reviews' : number_of_reviews
            })
        
        context = {
            'book_list' : book_list
        }

    return render(request, 'reviews/books_list.html', context)
