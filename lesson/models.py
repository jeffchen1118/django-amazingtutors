from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lessons")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Note(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="notes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
