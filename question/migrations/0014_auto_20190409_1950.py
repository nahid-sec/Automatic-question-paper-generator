# Generated by Django 2.1.5 on 2019-04-09 13:50

import django.contrib.auth.mixins
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.base


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0013_auto_20190318_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratePdf',
            fields=[
                ('questions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question.Questions')),
            ],
            bases=(django.contrib.auth.mixins.LoginRequiredMixin, django.views.generic.base.View, 'question.questions'),
        ),
        migrations.CreateModel(
            name='QuestionAdd',
            fields=[
                ('questions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question.Questions')),
            ],
            bases=(django.views.generic.base.View, 'question.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=models.TextField(default=''),
        ),
    ]