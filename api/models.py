from django.db import models

# Create your models here.
class Joke(models.Model):
    JOKE_CHOICES = [
        ('Roast', 'Roast'),
        ('Boast', 'Boast')
    ]
    body = models.CharField(max_length=280)
    joke_type = models.CharField(max_length=50, choices=JOKE_CHOICES)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    @property
    def total_likes(self):
        return self.upvote - self.downvote

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.body
