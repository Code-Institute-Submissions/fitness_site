from django.db import models
from django.utils import timezone
from fitness_project import settings


class Post(models.Model):
    #author = models.ForeignKey('auth.User', related_name='User')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
