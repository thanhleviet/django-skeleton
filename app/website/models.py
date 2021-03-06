from django.db import models

from core import models as core_models
from core.models import MODEL_STATUS, PUBLISHED


class Widget(core_models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    link_title = models.CharField(max_length=32)
    link_url = models.URLField()

    def __str__(self):
        return self.title


class Page(core_models.Model):
    status = models.CharField(max_length=9, choices=MODEL_STATUS, default=PUBLISHED)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    widgets = models.ManyToManyField(Widget)
    featured_image = models.ImageField(upload_to='website/page/', null=True, blank=True)

    def get_widgets(self):
        return self.widgets.all()

    def __str__(self):
        return self.title


class Category(core_models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class Post(core_models.Model):
    status = models.CharField(max_length=9, choices=MODEL_STATUS, default=PUBLISHED)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=32)
    short_content = models.CharField(max_length=512)
    full_content = models.TextField()
    categories = models.ManyToManyField(Category)
    featured_image = models.ImageField(upload_to='website/post/', null=True, blank=True)

    def __str__(self):
        return self.title


class Slider(core_models.Model):
    status = models.CharField(max_length=9, choices=MODEL_STATUS, default=PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class Slide(core_models.Model):
    status = models.CharField(max_length=9, choices=MODEL_STATUS, default=PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='website/slider/', null=True, blank=True)
    related_slider = models.ForeignKey(Slider)

    def __str__(self):
        return self.title


class Subscriber(core_models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.email)

