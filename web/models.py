from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=500, unique=False)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image_url = models.CharField(max_length=1000, unique=False)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('web-home')