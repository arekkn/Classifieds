from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Place(models.Model):
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place


class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)




