# Generated by Django 2.1.3 on 2018-12-21 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('author', models.ManyToManyField(to='read.Author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='BookNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notetitle', models.CharField(max_length=255)),
                ('notedate', models.DateField()),
                ('notetext', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read.Book')),
            ],
            options={
                'db_table': 'booknotes',
            },
        ),
        migrations.CreateModel(
            name='BooksRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datestarted', models.DateField()),
                ('dateended', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read.Book')),
            ],
            options={
                'db_table': 'booksread',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genrename', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='read.Genre'),
        ),
    ]
