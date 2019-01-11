from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from bleach import clean

from guides.utils import get_unique_slug

ALLOWED_TAGS = [
    'a', 'img', 'br', 'abbr', 'acronym', 'b', 'blockquote',
    'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'table',
    'h1', 'h2', 'h3', 'dl', 'dt', 'p', 'sup', 'strike', 'hr'
]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
    'img': ['src', 'width', 'height', 'alt', 'title']
}


class Guide(models.Model):
    category_choices = (
        ('pvm', 'PvM'),
        ('skilling', 'Habilidades'),
        ('other', 'Outros')
    )

    author = models.ForeignKey(verbose_name='Autor', to=User, related_name='guides', on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Título', max_length=25)
    slug = models.SlugField(max_length=35, unique=True)
    category = models.TextField(verbose_name='Categoria', max_length=30, choices=category_choices)
    description = models.TextField(verbose_name='Descrição', max_length=50)
    content = models.TextField(verbose_name='Conteúdo', max_length=5000)
    approved = models.BooleanField(verbose_name='Aprovado', default=False)
    date_posted = models.DateTimeField(verbose_name="Data", default=timezone.now)

    class Meta:
        verbose_name = 'Guia'
        verbose_name_plural = 'Guias'

    def save(self, *args, **kwargs):
        # Only create a slug on first save, thus title changes will not change the slug
        if not self.slug:
            # Creating a unique slug for the Guide
            self.slug = get_unique_slug(self, 'title', 'slug')

        # Cleaning content field to check for unsafe html,
        # any tags or attributes not listed below will be escaped/stripped
        self.content = clean(self.content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()

    def unapprove(self):
        self.approved = False
        self.save()
