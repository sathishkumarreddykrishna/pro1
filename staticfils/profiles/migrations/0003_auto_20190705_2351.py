# Generated by Django 2.1.7 on 2019-07-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='discription',
            field=models.TextField(default='discription default text'),
        ),
    ]
