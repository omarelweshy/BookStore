# Generated by Django 3.0.6 on 2020-06-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
