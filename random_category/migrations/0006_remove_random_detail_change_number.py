# Generated by Django 4.0 on 2021-12-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_category', '0005_remove_quote_autor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='random_detail',
            name='change_number',
        ),
    ]
