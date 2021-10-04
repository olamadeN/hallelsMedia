from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=300)
    slug = models.SlugField()
    thumbnail = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name

# contact us form
#class Contact(models.Model):
#   name = models.CharField(max_length=100)
#   email = models.EmailField()
#   message = models.TextField(max_length=300)

