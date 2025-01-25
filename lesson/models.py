from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, IntegerField, Value, When
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
QUESTIONTYPES = ((0, "Discussion"), (1, "Test"))


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

    # def get_ordered_answers(self):
    #     return self.answers.annotate(
    #         is_author=Case(
    #             When(owner=self.lesson.author, then=Value(1)),
    #             default=Value(0),
    #             output_field=IntegerField(),
    #         )
    #     ).order_by("-is_author", "created_on")


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()  # Field for storing the answer content
    try_attempt = models.IntegerField(default=0, blank=True, null=True)
    # likes = models.IntegerField(default=0)
    # liked_list = models.JSONField(default=list)  # Requires Django 3.1+
    grade = models.FloatField(default=0, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]
