# Generated by Django 4.2.10 on 2024-02-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.TextField(),
        ),
    ]
