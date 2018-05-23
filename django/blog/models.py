from django.db import models
from django.utils import timezone

# Sávio Gomes
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # este é um link para outro modelo.
    title = models.CharField(max_length=200)  # assim é como você define um texto com um número limitado de caracteres.
    text = models.TextField()        # este é para textos longos, sem um limite. Será ideal para um conteúdo de post de blog
    created_date = models.DateTimeField(default=timezone.now)     
    published_date = models.DateTimeField(blank=True, null=True)  


def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
