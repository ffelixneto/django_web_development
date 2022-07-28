
def average_rating(rating_list : list) -> int:
    """
    FUNÇÃO PARA RETORNAR A MEDIA DE CLASSIFICAÇÃO DO LIVRO
    """

    if not rating_list:
        return 0
    
    return round(sum(rating_list) / len(rating_list))