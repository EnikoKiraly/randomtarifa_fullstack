# Generated by Django 4.0 on 2021-12-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_category', '0003_alter_random_detail_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
    ]
