from bleach import clean
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from guides.utils import get_unique_slug

User = get_user_model()

ALLOWED_TAGS = [
    'a', 'img', 'br', 'abbr', 'acronym', 'b', 'blockquote', 'span',
    'code', 'em', 'i', 'li', 'ol', 'strong', 'ul', 'table',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6' 'dl', 'dt', 'p', 'sup', 'strike', 'hr',

]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'abbr': ['title'],
    'acronym': ['title'],
    'img': ['src', 'width', 'height', 'alt', 'title'],
    '*': ['style']
}
ALLOWED_STYLES = [
    'color', 'font-weight', 'text-align', 'text-decoration', 'font-size',
    'padding-right', 'padding-left', 'background-color'
]


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
    description = models.TextField(verbose_name='Descrição', max_length=40)
    content = models.TextField(verbose_name='Conteúdo')
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

        # Cleaning content field to remove unsafe html, any tags/attributes/etc not whitelisted will be escaped/stripped
        self.content = clean(self.content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, styles=ALLOWED_STYLES)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def approve(self):
        self.approved = True
        self.save()

    def unapprove(self):
        self.approved = False
        self.save()
