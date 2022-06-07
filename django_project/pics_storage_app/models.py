from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()

    class Meta:
        db_table = 'album'

    def __str__(self):
        return self.title
