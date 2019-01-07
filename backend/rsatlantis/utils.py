from django.utils.text import slugify


def get_unique_slug(model_instance, slugable_field_name, slug_field_name):
    """
    Source: https://fazle.me/auto-generating-unique-slug-django-generic-approach/

    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    model_class = model_instance.__class__
    # This is a very inefficient query, and will do a lot of db queries in case a specific
    # name is repeated a lot. Possibly needed change to a unique_slug that adds the model id
    # to the end of the title instead of this.
    while model_class._default_manager.filter(**{slug_field_name: unique_slug}).exists():
        unique_slug = f'{slug}-{extension}'
        extension += 1

    return unique_slug
