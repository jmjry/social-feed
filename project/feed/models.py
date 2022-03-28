from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Cascade will delete all users posts if their account is deleted
    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    # Creates the field for users to post content 
class Comment(models.Model):
    content = models.TextField(max_length=2000)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date_posted"]

    def __str__(self):
        return f"Comment by {self.author}"
