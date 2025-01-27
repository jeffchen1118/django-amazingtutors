from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
QUESTIONTYPES = ((0, "Discussion"), (1, "Test"))


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lessons")
    featured_image = CloudinaryField(
        "image", blank=True, null=True, default="placeholder"
    )
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


class Question(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="questions"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    body = (
        models.TextField()
    )  # Field for storing the question or assignment task or practice content
    preset_answer = models.TextField(
        blank=True, null=True
    )  # Field for storing the predetermined answer
    answer_hidden = models.BooleanField(default=True)
    try_limit = models.IntegerField(default=0, blank=True, null=True)
    questiontype = models.IntegerField(choices=QUESTIONTYPES, default=0)
    due_date = models.DateTimeField(
        blank=True, null=True, default=None
    )  # Field for storing the due date
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()  # Field for storing the answer content
    try_attempt = models.IntegerField(default=0, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class GradeFeedback(models.Model):
    answer = models.OneToOneField(
        Answer, on_delete=models.CASCADE, related_name="grade_feedback"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="grade_feedback"
    )
    grade = models.FloatField(default=0, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade
