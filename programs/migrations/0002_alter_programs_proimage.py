# Generated by Django 5.1.1 on 2024-09-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='proimage',
            field=models.IntegerField(default='media/img/course/01.png'),
        ),
    ]
