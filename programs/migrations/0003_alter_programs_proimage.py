# Generated by Django 5.1.1 on 2024-09-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_alter_programs_proimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='proimage',
            field=models.ImageField(default='media/img/course/01.png', upload_to=''),
        ),
    ]
