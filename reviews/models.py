from django.db import models
from django.contrib import auth

# PUBLISHER MODEL
class Publisher(models.Model):
    """
    A empresa editora dos livros.
    """
    name = models.CharField(max_length=80, help_text="Nome da editora.")
    website = models.URLField(help_text="Site da editora.")
    email = models.EmailField(help_text="Email da editora.")
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Publishers'
    
    def __str__(self) -> str:
        return self.name

# BOOK MODEL
class Book(models.Model):
    """
    O livro publicado
    """
    title = models.CharField(max_length=70, help_text="Título do livro.")
    publication_date = models.DateField(verbose_name="A data em que o livro foi publicado.")
    isbn = models.CharField(max_length=20, help_text="Numero ISBN do livro.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
       verbose_name_plural = 'Books'

    def __str__(self) -> str:
       return self.title


# CONTRIBUTOR MODEL
class Contributor(models.Model):
    """
    Um contribuidor do livro Ex. Author, editor, co-autor.
    """
    first_names = models.CharField(max_length=50, help_text="Nomes do contribuidor.")
    last_names = models.CharField(max_length=50, help_text="Sobrenomes do contribuidor.")
    email = models.EmailField(help_text="Email de contto do contribuidor.")
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
       verbose_name_plural = 'Contributors'

    def __str__(self) -> str:
       return self.first_names

# CONTRIBUTOR MODEL
class BookContributor(models.Model):
    """
    Tabela intermediaria entre livro e contribuidores
    """

    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Autor"
        CO_AUTHOR = "CO_AUTHOR", "Co-Autor"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    role = models.CharField(verbose_name="A função desempenhada pelo cnontribuidor no livro.", 
        choices=ContributionRole.choices, max_length=20
        )

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
       verbose_name_plural = 'Book Contributors'

    # def __str__(self) -> str:
    #    return self.DESCRITIVO_PADRAO_AQUI


# REVIEW MODEL
class Review(models.Model):
    """
    Uma análise sobre um livro
    """
    content = models.TextField(help_text="O texto da análise.")
    rating = models.IntegerField(help_text="A classificação que o analista concede ao livro.")
    creator = models.ForeignKey(auth.get_user_model(), help_text="O criador da análise.", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, help_text="O livro referenciado nessa análise.", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True, help_text="A data em que a análise foi criada.")
    updated_at = models.DateTimeField(null=True, auto_now = True, help_text="A data da ultima edição da análise.")

    class Meta:
       verbose_name_plural = 'Reviews'

    def __str__(self) -> str:
       return self.content