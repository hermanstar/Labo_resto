# Generated by Django 3.0.6 on 2020-06-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20200618_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]