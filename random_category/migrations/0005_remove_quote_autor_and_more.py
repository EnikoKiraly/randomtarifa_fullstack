# Generated by Django 4.0 on 2021-12-26 10:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_category', '0004_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='random_category',
            name='clicks_number',
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
