# Generated by Django 2.1.5 on 2019-04-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0014_auto_20190409_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=models.TextField(default='Please describes your question..'),
        ),
    ]
