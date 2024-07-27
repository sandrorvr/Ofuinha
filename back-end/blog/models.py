from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify


class Posts(models.Model):
    categoryPost = models.CharField('Category', max_length=50)
    titlePost = models.CharField('Title', max_length=120)
    descriptionPost = models.CharField('Description', max_length=220)
    image = StdImageField(upload_to='articles', variations={'thumbnail': {"width": 292, "height": 330, "crop": True}})
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return  str(self.titlePost)
    
class PostDetail(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    contentPost = models.TextField('Content')