# Generated by Django 2.1.7 on 2019-03-14 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]
