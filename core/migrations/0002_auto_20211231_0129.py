# Generated by Django 3.0.7 on 2021-12-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='short_url',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]