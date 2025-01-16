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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson_section(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="sections"
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    order = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson_section, self).save(*args, **kwargs)

    class Meta:
        unique_together = ["lesson", "order"]
        ordering = ["order"]

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.ForeignKey(
        Lesson_section, on_delete=models.CASCADE, related_name="notes"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note {self.title} by {self.author}"
