# Generated by Django 3.0.4 on 2020-03-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.FilePathField(default='', path='img'),
            preserve_default=False,
        ),
    ]
