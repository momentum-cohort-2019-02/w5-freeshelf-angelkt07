# Generated by Django 2.1.7 on 2019-03-17 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_shelf', '0006_auto_20190317_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]
