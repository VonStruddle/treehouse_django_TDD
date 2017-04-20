from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    performer = models.ForeignKey('Performer', related_name='songs')
    length = models.IntegerField()

    def __str__(self):
        return '{0} by {1}'.format(self.title, self.artist)


class Performer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
