# Generated by Django 2.1.3 on 2018-12-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksread',
            name='reread',
            field=models.CharField(default='No', max_length=3),
            preserve_default=False,
        ),
    ]
