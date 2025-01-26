from django import template
from django.db.models import Case, IntegerField, Value, When

register = template.Library()


@register.filter
def user_in_answers(answers, user):
    return answers.filter(owner=user).exists()


# def user_in_answers(user, answers):
#     return any(answer.owner == user for answer in answers)


@register.filter
def order_answers_by_author(answers, lesson_author):
    return answers.annotate(
        is_author=Case(
            When(owner=lesson_author, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).order_by("-is_author", "created_on")
