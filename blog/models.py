from django.db import models

# Create your models here.


class blogModel(models.Model):
    title = models.CharField(max_length=100, blank=False)
    details = models.CharField(max_length=200, blank=False)
    time = models.DateTimeField()
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title
