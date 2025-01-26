# Generated by Django 4.2.17 on 2025-01-26 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lesson', '0007_alter_gradefeedback_answer_alter_gradefeedback_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradefeedback',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_feedback', to=settings.AUTH_USER_MODEL),
        ),
    ]
