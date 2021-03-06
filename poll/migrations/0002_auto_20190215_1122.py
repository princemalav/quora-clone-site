# Generated by Django 2.0.5 on 2019-02-15 05:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='down_list',
            field=models.ManyToManyField(related_name='ans_down_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='up_list',
            field=models.ManyToManyField(related_name='ans_up_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='down_list',
            field=models.ManyToManyField(related_name='que_down_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='up_list',
            field=models.ManyToManyField(related_name='que_up_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
