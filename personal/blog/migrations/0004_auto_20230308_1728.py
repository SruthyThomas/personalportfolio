# Generated by Django 3.0 on 2023-03-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230306_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
