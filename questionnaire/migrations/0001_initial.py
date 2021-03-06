# Generated by Django 3.2.12 on 2022-05-10 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=1000)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording', models.FileField(upload_to='')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.questionnaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
