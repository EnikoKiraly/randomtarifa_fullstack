# Generated by Django 4.0 on 2021-12-25 17:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_category', '0002_remove_random_detail_sharing_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='random_detail',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
