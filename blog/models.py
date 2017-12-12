from django.db import models
from django.utils import timezone
from django.conf import settings as django_settings



class Post(models.Model):
    #author = models.ForeignKey('auth.User', related_name='User')
    author = models.ForeignKey(django_settings.AUTH_USER_MODEL, related_name='User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
