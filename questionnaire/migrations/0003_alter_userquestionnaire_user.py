# Generated by Django 3.2.12 on 2022-05-14 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userregistration', '0001_initial'),
        ('questionnaire', '0002_auto_20220510_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestionnaire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userregistration.userregistration'),
        ),
    ]