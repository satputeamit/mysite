from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)
    text=models.TextField()
    created=models.DateTimeField()

    class Meta:
        ordering=('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])


# Create your models here.
