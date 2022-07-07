from django.shortcuts import render

def index(request):
    """
    FUNÇÃO INICIAL PARA A VIEW DE REVIEWS
    """

    name = "Sol"
    
    return render(request, "base.html", {"name" : name})
